# -*- coding:utf-8 -*-

from common import logger, Functions, Openpage
from common import CryptoMarkets
from common.HTMLReport import BeautifulReport
from PIL import Image as img
import unittest
import sys
import os
import time
import platform




logger.__DEBUG__ = True

loggers = logger.Logger(__name__).log()


def get_log():
    return loggers


def get_img_path():
    img_path = '/TestFiles/img/' if platform.system() != 'Windows' else '\\TestFiles\\img'
    abs_img_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0] + img_path
    return abs_img_path
get_img_path()