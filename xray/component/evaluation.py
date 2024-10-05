from importlib.util import module_from_spec
import sys
from typing import Tuple

import torch
from torch.nn import *
from torch.nn import CrossEntropyLoss, Module
from torch.optim import SGD, Optimizer
from torch.utils.data import DataLoader

from xray.entity.artifact_entity import (
    DataTransformationArtifact,
    ModelEvaluationArtifact,
    ModelTrainerArtifact,
)
from xray.entity.config_entity import ModelEvaluationConfig
from xray.exception import CustomException
from xray.logger import logging
from xray.ml.architecture import Net

class ModelEvaluation:
    def __init__(
        self,
        data_transformation_artifact : DataTransformationArtifact,
        model_trainer_artifact: ModelTrainerArtifact,
        model_evaluation_config: ModelEvaluationConfig,
    ):
        self.data_transformation_artifact = data_transformation_artifact
        self.model_trainer_artifact = model_trainer_artifact
        self.model_evaluation_config = model_evaluation_config

    def configuration(self) -> Tuple[DataLoader, Module, float, Optimizer]:
        try:
            logging.info("Entered the configuration method of ModelEvaluation class")
            
            test_dataloader: DataLoader = self.data_transformation_artifact.transformed_test_object
            
            model: Module = Net()  # Initialize the model
            model.load_state_dict(torch.load(self.model_trainer_artifact.trained_model_path))  # Load the state dict
            model.eval()  # Set the model to evaluation mode
            
            cost: Module = CrossEntropyLoss()
            
            logging.info("Exited from configuration in the model Evaluation")
            
            return test_dataloader, model, cost
        except Exception as e:
            raise CustomException(e, sys)


    import torchmetrics  # Optional if you want to use metrics package for simplicity.

    def test_net(self) -> Tuple[float, float, float, float]:
        logging.info("Entered the test_net method of ModelEvaluation class")

        try:
            # Load test data, model, and loss function from configuration
            test_dataloader, net, cost = self.configuration()

            # Metrics initialization
            correct_predictions = 0
            total_predictions = 0
            true_positives = 0
            false_positives = 0
            false_negatives = 0

            with torch.no_grad():
                for _, data in enumerate(test_dataloader):
                    images = data[0].to(self.model_evaluation_config.device)
                    labels = data[1].to(self.model_evaluation_config.device)

                    # Model predictions
                    output = net(images)
                    loss = cost(output, labels)
                    predictions = torch.argmax(output, dim=1)

                    # Update overall metrics
                    correct_predictions += (predictions == labels).sum().item()
                    total_predictions += labels.size(0)

                    # Calculate true positives, false positives, and false negatives
                    true_positives += ((predictions == 1) & (labels == 1)).sum().item()
                    false_positives += ((predictions == 1) & (labels == 0)).sum().item()
                    false_negatives += ((predictions == 0) & (labels == 1)).sum().item()

                    # Log loss and intermediate details
                    logging.info(
                        f"Actual_Labels : {labels}     Predictions : {predictions}     Loss : {loss.item():.4f}"
                    )

                    self.model_evaluation_config.test_loss += loss.item()
                    self.model_evaluation_config.total_batch += 1

                # Calculate accuracy, precision, recall, F1-score
                accuracy = (correct_predictions / total_predictions) * 100

                # Avoid division by zero
                precision = (
                    true_positives / (true_positives + false_positives)
                    if (true_positives + false_positives) > 0
                    else 0
                )
                recall = (
                    true_positives / (true_positives + false_negatives)
                    if (true_positives + false_negatives) > 0
                    else 0
                )
                f1_score = (
                    2 * (precision * recall) / (precision + recall)
                    if (precision + recall) > 0
                    else 0
                )

                logging.info(f"Model Accuracy: {accuracy:.2f}%")
                logging.info(f"Model Precision: {precision:.4f}")
                logging.info(f"Model Recall: {recall:.4f}")
                logging.info(f"Model F1-Score: {f1_score:.4f}")

                logging.info("Exited the test_net method of Model evaluation class")

                return accuracy, precision, recall, f1_score

        except Exception as e:
            raise CustomException(e, sys)


    def initiate_model_evaluation(self) -> ModelEvaluationArtifact:
        logging.info("Entered the initiate_model_evaluation method of Model evaluation class")

        try:
            # Call test_net to get all evaluation metrics
            accuracy, precision, recall, f1_score = self.test_net()

            # Create ModelEvaluationArtifact with all metrics
            model_evaluation_artifact: ModelEvaluationArtifact = ModelEvaluationArtifact(
                model_accuracy=accuracy,
                model_precision=precision,
                model_recall=recall,
                model_f1_score=f1_score,
            )

            logging.info("Exited the initiate_model_evaluation method of Model evaluation class")

            return model_evaluation_artifact

        except Exception as e:
            raise CustomException(e, sys)
