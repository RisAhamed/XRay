import os
from dataclasses import dataclass
from xray.constants.training_pipeline import *

# Define artifact_dir globally to avoid initializing it repeatedly
ARTIFACT_DIR_GLOBAL = os.path.join(ARTIFACT_DIR, TIMESTAMP)

@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.s3_data_folder: str = S3_DATA_FOLDER

        self.bucket_name: str = BUCKET_NAME

        # Use the global artifact_dir
        self.artifact_dir: str = ARTIFACT_DIR_GLOBAL

        self.data_path: str = os.path.join(
            self.artifact_dir, "data_ingestion", self.s3_data_folder
        )

        self.train_data_path: str = os.path.join(self.data_path, "train")

        self.test_data_path: str = os.path.join(self.data_path, "test")


@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.color_jitter_transforms: dict = {
            "brightness": BRIGHTNESS,
            "contrast": CONTRAST,
            "saturation": SATURATION,
            "hue": HUE,
        }

        self.RESIZE: int = RESIZE

        self.CENTERCROP: int = CENTERCROP

        self.RANDOMROTATION: int = RANDOMROTATION

        self.normalize_transforms: dict = {
            "mean": NORMALIZE_LIST_1,
            "std": NORMALIZE_LIST_2,
        }

        self.data_loader_params: dict = {
            "batch_size": BATCH_SIZE,
            "shuffle": SHUFFLE,
            "pin_memory": PIN_MEMORY,
        }

        # Use the global artifact_dir
        self.artifact_dir: str = os.path.join( ARTIFACT_DIR_GLOBAL,"Data_transformation")

        self.train_transforms_file: str = os.path.join(
            self.artifact_dir, TRAIN_TRANSFORMS_FILE
        )

        self.test_transforms_file: str = os.path.join(
            self.artifact_dir, TEST_TRANSFORMS_FILE
        )



@dataclass
class ModelTrainerConfig:
    def __init__(self):
        self.artifact_dir = os.path.join(ARTIFACT_DIR_GLOBAL,"Model-Trainer")
        self.trained_bentoml_model_name: str ="xraymodel"

        self.trained_model_path: int = os.path.join(
            self.artifact_dir, TRAINED_MODEL_NAME
        )
        self.train_transforms_key : str = TRAIN_TRANSFORMS_KEY
        self.epochs: int = EPOCH

        self.optimizer_params : dict = {'lr':0.05,'momentum': 0.7}
        self.scheduler_params: dict = {'step_size':STEP_SIZE,'gamma': GAMMA}
        # self.criterion_params: dict = {'weight': WEIGHT}
        self.device = DEVICE



@dataclass
class ModelEvaluationConfig:
    def __init__(self):
        self.device  = DEVICE

        self.test_loss :int = 0
        self.test_accuracy : int = 0
        self.total : int = 0
        self.total_batch : int = 0

        self.optimizer_params : dict = {'lr': 0.01,'momentum':  0.01}
         

@dataclass
class ModelPusherConfig:
    def __init__(self):
        self.bentoml_model_name: str = BENTOML_MODEL_NAME

        self.bentoml_service_name: str = BENTOML_SERVICE_NAME

        self.train_transforms_key: str = TRAIN_TRANSFORMS_KEY

        self.bentoml_ecr_image: str = BENTOML_ECR_URI
