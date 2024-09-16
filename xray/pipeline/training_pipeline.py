import sys
from xray.exception import CustomException
from xray.component.ingestion import DataIngestion
from xray.component.transformation import DataTransformation
from xray.entity.config_entity import *
from xray.entity.artifact_entity import *
from xray.logger import logging

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config  = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()  # Initialize DataTransformationConfig with default values

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
        
    def start_data_transformation(self, data_ingestion_artifact: DataIngestionArtifacts) -> DataTransformationArtifacts:
        
        logging.info("Entered the start_data_transformation method of TrainPipeline class")

        try:
            data_transformation = DataTransformation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_transformation_config=self.data_transformation_config,
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
    def run_pipleine(self)-> None:
        logging.info("Starting the training pipeline")
        data_ingestion_Artifacts: DataIngestionArtifacts = self.start_data_ingestion()
        data_transformation_Artifacts : DataTransformationArtifacts =self.start_data_transformation(data_ingestion_artifact=data_ingestion_Artifacts)

        logging.info('completed Triing Pipeline')

# if __name__ == "__main__":
#     training_pipeline =TrainPipeline()
#     training_pipeline.start_data_ingestion()