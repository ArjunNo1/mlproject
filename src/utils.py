import os,sys
import pandas as pd
import numpy as np
from src.exception import MyException
import dill

def save_object(file_path,object):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path,'wb') as file:
            dill.dump(object,file)
    except Exception as e:
        raise MyException(sys.exc_info())
    