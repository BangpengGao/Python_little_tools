# -*- coding: utf-8 -*-
# @Author: Phill
# @Date:   2019-05-28 10:40:39
# @Last Modified by:   Phill
# @Last Modified time: 2019-05-28 10:40:53

import logging

logging.basicConfig(filename="test.log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')