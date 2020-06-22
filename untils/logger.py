# user/bin/python3
import logging
import sys


def init_logger(level=logging.DEBUG):
    """
    :return: None if success
    """
    if level == logging.DEBUG:
        log_format = "%(levelname)s: [%(module)s/%(funcName)s:%(lineno)d] | %(message)s"
    else:
        log_format = "%(levelname)s: [%(module)s/%(funcName)s] | %(message)s"
    logging.basicConfig(level=level, format=log_format, datefmt="%Y-%m-%d %H:%M:%S")
