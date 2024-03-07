import logging
import sys

def exception_handler( error_details):
    filename = error_details[2].tb_frame.f_code.co_filename
    lineno = error_details[2].tb_lineno
    exception_type = error_details[0].__name__
    error_message = "Error occurred on File: {0},\nLine: {1}\nException-Type: {2}\nUnpack : {3}".format(
        filename,
        lineno,
        exception_type,(error_details[0]
                        ,error_details[1]
                         ,error_details[2]
                         ))
    return error_message

class MyException(Exception):
    def __init__(self,error_details):
        super().__init__(error_details)
        self.error = exception_handler(error_details)

    def __str__(self):
        return self.error
# try:
#     # Code that might raise an exception
#     1 / 0
# except Exception as e:
#     # obj = MyException(sys.exc_info())
#     # print(obj)
#     logging.info("Hello Exception Occured")
#     raise MyException(sys.exc_info())
