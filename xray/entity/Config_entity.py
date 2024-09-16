import os
from dataclasses import dataclass
from torch import device
from xray.constants.training_pipeline import *

# @dataclass
# class DataIngestionConfig:
#     def __init__(self):
#         self.s3_data_folder = S3_DATA_FOLDER
#         self.artifact_dir = os.path.join(ARTIFACT_DIR,TIMESTAMP)
#         self.bucket_name =  BUCKET_NAME

#         self.data_path : str = os.path.join(
#             self.artifact_dir,"data_ingesition",self.s3_data_folder)
        
    
#         self.train_data_path :str = os.path.join(self.data_path,'train')

#         self.test_data_path :str = os.path.join(self.data_path,'test')
from pathlib import Path

@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.s3_data_folder = S3_DATA_FOLDER
        self.artifact_dir = os.path.join(ARTIFACT_DIR,TIMESTAMP)
        self.bucket_name =  BUCKET_NAME

        self.data_path : str = os.path.join(
            self.artifact_dir,"data_ingestion",self.s3_data_folder)
        
        # Create the data directory if it doesn't exist
        os.makedirs(self.data_path, exist_ok=True)

        self.train_data_path :str = os.path.join(self.data_path,'train')
        self.test_data_path :str = os.path.join(self.data_path,'test')

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
        self.artifact_dir = os.path.join(ARTIFACT_DIR,TIMESTAMP,"data_transformation")
        self.train_transform_file= os.path.join(self.artifact_dir,"train_transform")
        self.test_transform_file = os.path.join(self.artifact_dir,"test_transform")