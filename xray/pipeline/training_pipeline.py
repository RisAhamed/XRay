import sys
from xray.exception import CustomException
from xray.component.ingestion import DataIngestion
from xray.entity.config_entity import DataIngestionConfig
from xray.entity.artifact_entity import *
from xray.logger import logging

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config  = DataIngestionConfig()

    def start_data_ingestion(self)-> DataIngestionArtifacts:
        try:
            logging.info("Starting data ingestion")
            ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)
            data_ingestion_artifacts = ingestion.initiate_data_ingestion()

           
            logging.info("Got the train_set and test_set from s3")

            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )
            return data_ingestion_artifacts
        
        except Exception as e:
            logging.error(f"Error occurred while starting data ingestion: {str(e)}")
            raise CustomException(e,sys)
        
    def run_pipleine(self)-> None:
        logging.info("Starting the training pipeline")
        data_ingestion_Artifacts: DataIngestionArtifacts = self.start_data_ingestion()

        logging.info('completed Triing Pipeline')

# if __name__ == "__main__":
#     training_pipeline =TrainPipeline()
#     training_pipeline.start_data_ingestion()