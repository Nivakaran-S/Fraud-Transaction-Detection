from FraudTransactionDetection.components.data_ingestion import DataIngestion
from FraudTransactionDetection.components.data_validation import DataValidation
from FraudTransactionDetection.components.data_transformation import DataTransformation
from FraudTransactionDetection.components.model_trainer import ModelTrainer

from FraudTransactionDetection.exception.exception import FraudTransactionException
from FraudTransactionDetection.logging.logger import logging 
from FraudTransactionDetection.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from FraudTransactionDetection.entity.config_entity import TrainingPipelineConfig

import sys 

if __name__=='__main__':
    try:
        trainingPipelineConfig=TrainingPipelineConfig()
        dataIngestionConfig=DataIngestionConfig(trainingPipelineConfig)
        dataIngestion=DataIngestion(dataIngestionConfig)
        logging.info("Initiate the data ingestion")
        dataIngestionArtifact=dataIngestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataIngestionArtifact)

        dataValidationConfig=DataValidationConfig(trainingPipelineConfig)
        dataValidation=DataValidation(dataIngestionArtifact, dataValidationConfig)
        logging.info("Initiate the data Validation")
        dataValidationArtifact=dataValidation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(dataValidationArtifact)

        dataTransformationConfig=DataTransformationConfig(trainingPipelineConfig)
        logging.info("Data Transformation started")
        dataTransformation=DataTransformation(dataValidationArtifact, dataTransformationConfig)
        dataTransformationArtifact=dataTransformation.initiate_data_transformation()
        print(dataTransformationArtifact)
        logging.info("Data Transformation Completed")

        logging.info("Model Training started")
        modelTrainerConfig=ModelTrainerConfig(trainingPipelineConfig)
        modelTrainer=ModelTrainer(model_trainer_config=modelTrainerConfig, data_transformation_artifact=dataTransformationArtifact)
        modelTrainerArtifact=modelTrainer.initiate_model_trainer()

        logging.info("Model Training artifact created")



    except Exception as e:
        raise FraudTransactionException(e, sys)