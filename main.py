import sys
from chicken_disease_classification.logger import logging
from chicken_disease_classification.exception import CustomException
from chicken_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline




STAGE_NAME="Data Ingestion Stage"
try:
    logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e, sys)