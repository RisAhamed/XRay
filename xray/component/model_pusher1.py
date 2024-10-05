import os
import sys

from sqlalchemy import custom_op

from xray.entity.artifact_entity import ModelPusherArtifact
from xray.entity.config_entity import ModelPusherConfig
from xray.exception import CustomException
from xray.logger import logging
# from xray.cloud_Storage.s3_operations import *
from xray.cloud_Storage.s3_ops import *

class ModelPusher:
    def __init__(self,model_pusher_config: ModelPusherConfig):

        self.model_pusher_config = model_pusher_config
        self.s3 = S3Operation()


    
    def initiate_model_pusher(self):

        """
        Method Name :   initiate_model_pusher

        Description :   This method initiates model pusher. 
        
        Output      :    Model pusher artifact 
        """
        logging.info("Entered initiate_model_pusher method of Modelpusher class")
        try:
            # Uploading the best model to s3 bucket
            self.s3.upload_file(
                "ml/model/model.pt",
                "model.pt",
                "lungxray24",
                remove=False,
            )
            logging.info("Uploaded best model to s3 bucket")
            logging.info("Exited initiate_model_pusher method of ModelTrainer class")


        except Exception as e:
            raise CustomException(e,sys)
