import sys
from chicken_disease_classification.logger import logging
from chicken_disease_classification.exception import CustomException
from chicken_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chicken_disease_classification.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from chicken_disease_classification.pipeline.stage_03_prepare_base_model import PrepareBaseModelTrainingPipeline
from chicken_disease_classification.pipeline.stage_04_training import ModelTrainingPipeline
from chicken_disease_classification.pipeline.stage_05_evaluation import EvaluationPipeline




STAGE_NAME="Data Ingestion Stage"
try:
    logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e, sys)


STAGE_NAME="Data Validation Stage"
try:
    logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e, sys)


STAGE_NAME = "Prepare Base Model stage"
try:
    logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e, sys)

STAGE_NAME = "Training stage"
try:
    logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    training = ModelTrainingPipeline()
    training.main()
    logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e, sys)


STAGE_NAME = "Model Evaluation stage"
try:
    logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    evaluation = EvaluationPipeline()
    evaluation.main()
    logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e, sys)