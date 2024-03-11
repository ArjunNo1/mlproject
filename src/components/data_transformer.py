import sys
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from src.logger import logging
from src.exception import MyException
from src.utils import save_object
from dataclasses import dataclass

@dataclass

class DataTransformerConfig:
    preprocessor_filepath = os.path.join("artifact","preprocessor.pkl")

class DataTransformer:
    def __init__(self):
        self.transformer = DataTransformerConfig()

    def transform(self):
        try:

            numerical_features = ['math score', 'writing score']
            categorical_features = ['gender', 'race/ethnicity', 'parental level of education', 'lunch', 
                                    'test preparation course']
            
            logging.info("Creating numerical pipeline")

            numerical_pipeline = Pipeline(steps=[
                    ('Imputer', SimpleImputer(strategy='median')),
                    ('Standardscaler', StandardScaler())  # Set with_mean=False for sparse matrices
                ])

            categorical_pipeline = Pipeline(steps=[
                ('Imputer', SimpleImputer(strategy='most_frequent')),
                ('OneHotEncoding', OneHotEncoder()),
            ])

            preprocessor = ColumnTransformer(
                    transformers=[
                    ('Numerical', numerical_pipeline, numerical_features),
                    ('Categorical', categorical_pipeline, categorical_features)
                ]
            )

            logging.info("Creating categorical pipeline")

            
            logging.info("Column transformer created")
        
            return preprocessor
            
        except Exception as e:
            raise MyException(sys.exc_info())
        

    def start_data_transformation(self,train_path,test_path):
        try:
            traindata = pd.read_csv(train_path)
            testdata = pd.read_csv(test_path)
            preprocessed_object = self.transform()

            target = "reading score"
            numerical_features = ["math score", "writing score"]

            input_X_train = traindata.drop(columns=[target],axis =1)

            target_y_train = traindata[target]

            input_X_test = testdata.drop(columns=[target],axis=1)
            target_y_test = testdata[target]

            preprocessed_train = preprocessed_object.fit_transform(input_X_train)
            
            preprocessed_test = preprocessed_object.transform(input_X_test)

            train_arr = np.c_[preprocessed_train, np.array(target_y_train)]
            test_arr = np.c_[preprocessed_test, np.array(target_y_test)]


            #Save the preprocessor object
            logging.info("Saving preprocessor object")

            save_object(file_path = self.transformer.preprocessor_filepath,
                        object = preprocessed_object)
            logging.info("Preprocessor object saved")
            return (train_arr,
                    test_arr)
        
        except Exception as e:
            raise MyException(sys.exc_info())

        
    
    