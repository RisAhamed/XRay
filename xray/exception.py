# custom_exception.py

import sys
import traceback

class CustomException(Exception):
    def __init__(self, exception, sys):
        self.exception = exception
        self.file_name = sys.exc_info()[2].tb_frame.f_code.co_filename
        self.line_number = sys.exc_info()[2].tb_lineno
        self.full_traceback = traceback.format_exc()

    def __str__(self):
        return f"""
        Error Message: {str(self.exception)}
        File Name: {self.file_name}
        Line Number: {self.line_number}
        Full Traceback:
        {self.full_traceback}
        """

    def get_error_details(self):
        return {
            "error_message": str(self.exception),
            "file_name": self.file_name,
            "line_number": self.line_number,
            "full_traceback": self.full_traceback,
        }