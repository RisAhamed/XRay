import os
from dataclasses import dataclass
from torch import device
from xray.constants.training_pipeline import *

@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.s3_data_folder = S3_DATA_FOLDER
        self.artifact_dir = os.path.join(ARTIFACT_DIR,TIMESTAMP)
        self.bucket_name =  BUCKET_NAME

        self.data_path : str = os.path.join(
            self.artifact_dir,"data_ingesition",self.s3_data_folder)
        
    
        self.train_data_path :str = os.path.join(self.data_path,'train')

        self.test_data_path :str = os.path.join(self.data_path,'test')

