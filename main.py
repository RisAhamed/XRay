from xray.pipeline.training_pipeline import TrainPipeline
from xray.exception import CustomException
import sys

try:
        
    training_pipeline =TrainPipeline()
    training_pipeline.run_pipleine()

except Exception as e:
    raise CustomException(e,sys)