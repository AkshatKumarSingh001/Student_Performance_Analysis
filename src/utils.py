'''
Utils.py is a utility module that contains helper functions and classes used throughout the project. It provides common functionalities that can be reused in different parts of the codebase.

'''

import pickle
import os
import sys
import numpy as np
import pandas as pd
import dill

from src.exception import CustomException


def save_object(file_path, obj):
    '''
    This function saves a Python object to a specified file path using the pickle module.
    
    Args:
        file_path (str): The path where the object will be saved.
        obj (object): The Python object to be saved.
    
    Raises:
        CustomException: If there is an error while saving the object.
    '''
    try:
        dir_path = os.path.dirname(file_path) # Get the directory path from the file path.
        os.makedirs(dir_path, exist_ok=True) # Create the directory if it doesn't exist.

        with open(file_path, 'wb') as file_obj: # Open the file in write-binary mode.
            dill.dump(obj, file_obj) # Save the object to the file using pickle.

    except Exception as e:
        raise CustomException(e, sys) # Raise a custom exception if any error occurs while saving the object.
