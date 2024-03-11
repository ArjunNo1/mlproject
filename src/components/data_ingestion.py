import os,sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformer import DataTransformerConfig
from src.components.data_transformer import DataTransformer
from src.logger import logging
from src.exception import MyException

@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("artifact","train.csv")
    test_data_path = os.path.join("artifact","test.csv")
    raw_data_path = os.path.join("artifact","raw_data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion = DataIngestionConfig()

    def start_ingestion(self):
        logging.info("Data Ingestion Started")

        try:
            df=pd.read_csv(r"C:\Users\BaAr349\Personal\mlproject\notebook\data\StudentsPerformance.csv")
            print(df.head(1))
            logging.info("Data Ingested Successfully")
            artifact_path =os.path.join(os.getcwd(),"artifact")

            os.makedirs(artifact_path,exist_ok = True)

            df.to_csv(self.ingestion.raw_data_path,index=False)
            logging.info("Raw data saved successfully")

            train,test = train_test_split(df,test_size=0.25,random_state=42)
            train.to_csv(self.ingestion.train_data_path,index=False)
            test.to_csv(self.ingestion.test_data_path,index=False)
            logging.info("Train and Test data saved successfully")

            return self.ingestion.train_data_path,self.ingestion.test_data_path
            
        except Exception as e:
            raise MyException(sys.exc_info())


if __name__=="__main__":
    obj = DataIngestion()
    print("bvfhv")
    trainDatapath,testDatapath = obj.start_ingestion()
    logging.info("Data Ingestion Completed")

    data_transformer = DataTransformer()
    print("transforming data")
    # preprocess = data_transformer.transform()
    # print(preprocess)
    data_transformer.start_data_transformation(trainDatapath,testDatapath)
    logging.info("Data Transformation Completed")
