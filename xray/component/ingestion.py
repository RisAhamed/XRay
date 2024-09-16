from xray.logger import logging
from xray.exception import CustomException
import sys
from xray.cloud_Storage.s3_operations import S3Operations
from xray.entity.artifact_entity import *
from xray.entity.config_entity import * 
class DataIngestion:
    def __init__(self,data_ingestion_config: DataIngestionConfig):

        self.data_ingestion_config = data_ingestion_config
        self.s3 = S3Operations()
    def get_data_from_s3(self):

        try:
            logging.info("Entered the get_data_from_s3 method of Data ingestion class")

            self.s3.sync_folder_from_s3(
                folder=self.data_ingestion_config.data_path,
                bucket_name=self.data_ingestion_config.bucket_name,
                bucket_folder_name=self.data_ingestion_config.s3_data_folder,
            )

            logging.info("Exited the get_data_from_s3 method of Data ingestion class")


        except Exception as e:
            raise CustomException(e,sys)
    def initiate_data_ingestion(self):
        logging.info("Starting data ingestion")
        try :
            self.get_data_from_s3()
            data_ingestion_artifacts: DataIngestionArtifacts = DataIngestionArtifacts(
                train_file_path=self.data_ingestion_config.train_data_path,
                test_file_path=self.data_ingestion_config.test_data_path
            ) 
            logging.info("Data ingestion artifacts completed")

            return data_ingestion_artifacts
        
        except Exception as e:
            raise CustomException(e,sys)