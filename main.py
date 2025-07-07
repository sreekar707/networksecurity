from networksecurityy.components.data_ingestion import DataIngestion
from networksecurityy.exception.exception import NetworkSecurityException
from networksecurityy.logging.logger import logging
from networksecurityy.entity.config_entity import DataIngestionConfig
from networksecurityy.entity.config_entity import TrainingPipelineConfig
import sys


if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        
    except Exception as e:
           raise NetworkSecurityException(e,sys)