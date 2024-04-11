import sys


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  ## exc info jayega exception k pass or mere ko massage fetch kr k dejayega 

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class CustomException(Exception): ## parent class ko inherient kiya hai 
    def __init__(self, error_message, error_detail: sys):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message) ## parent class ko Call kiya hai 

        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):  ## if error come then gives massage 
        return self.error_message
