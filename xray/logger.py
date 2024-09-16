# import logging
# import os

# from xray.constants.training_pipeline import TIMESTAMP

# LOG_FILE: str = f"{TIMESTAMP}.log"

# logs_path = os.path.join(os.getcwd(), "logs", TIMESTAMP)

# os.makedirs(logs_path, exist_ok=True)

# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )


# logger.py

import logging
import os
from xray.constants.training_pipeline import TIMESTAMP

class Logger:
    def __init__(self):
        self.log_dir = os.path.join(os.getcwd(), "logs", TIMESTAMP)
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file = f"{TIMESTAMP}.log"
        self.log_file_path = os.path.join(self.log_dir, self.log_file)

    def create_logger(self):
        logging_str = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
        logger = logging.getLogger("X_RAY_logger")
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(self.log_file_path)
        stream_handler = logging.StreamHandler()

        file_handler.setFormatter(logging.Formatter(logging_str))
        stream_handler.setFormatter(logging.Formatter(logging_str))

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        return logger

logger_obj = Logger()
logging= logger_obj.create_logger()