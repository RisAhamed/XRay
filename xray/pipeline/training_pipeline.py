import sys
from xray.exception import CustomException
from xray.component.ingestion import DataIngestion
from xray.component.transformation import DataTransformation
from xray.component.model_trainer import ModelTrainer
from xray.entity.config_entity import *
from xray.entity.artifact_entity import *
from xray.logger import logging

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.model_trainer_config = ModelTrainerConfig()
        # self.model_evaluation_config=ModelEvaluationConfig()
        # self.model_pusher_config = ModelPusherConfig()
        
        
    def start_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:

            logging.info("Getting the data from s3 bucket")

            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config,
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info("Got the train_set and test_set from s3")

            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact

        
        except Exception as e:
            logging.error(f"Error occurred while starting data ingestion: {str(e)}")
            raise CustomException(e,sys)
        
    def start_data_transformation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataTransformationArtifact:
        
        logging.info("Entered the start_data_transformation method of TrainPipeline class")

        try:
            data_transformation = DataTransformation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_transformation_config= self.data_transformation_config,
            )

            data_transformation_artifact = (
                data_transformation.initiate_data_transformation()
            )

            logging.info(
                "Exited the start_data_transformation method of TrainPipeline class"
            )

            return data_transformation_artifact

        except Exception as e:
            raise CustomException(e, sys)
        
    def start_model_trainer(self, data_transformation_artifact: DataTransformationArtifact) -> ModelTrainerArtifact:
        logging.info("Entered the start_model_trainer method of TrainPipeline class")

        try:
            model_trainer = ModelTrainer(
                data_transformation_artifact=data_transformation_artifact,
                model_trainer_config=self.model_trainer_config,
            )

            model_trainer_artifact = model_trainer.initiate_model_trainer()

            logging.info("Exited the start_model_trainer method of TrainPipeline class")

            return model_trainer_artifact

        except Exception as e:
            raise CustomException(e, sys)
    def run_pipleine(self)-> None:
        logging.info("Starting the training pipeline")
        data_ingestion_Artifacts: DataIngestionArtifact = self.start_data_ingestion()
        data_transformation_Artifacts : DataTransformationArtifact =self.start_data_transformation(data_ingestion_artifact=data_ingestion_Artifacts)
        
        model_trainer_artifact: ModelTrainerArtifact = self.start_model_trainer(
                data_transformation_artifact=data_transformation_Artifacts
            )
        logging.info('completed Triing Pipeline ')

# if __name__ == "__main__":
#     training_pipeline =TrainPipeline()
#     training_pipeline.start_data_ingestion()