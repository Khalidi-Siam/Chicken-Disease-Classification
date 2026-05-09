import sys
from chicken_disease_classification.exception import CustomException
from chicken_disease_classification.config.configuration import ConfigurationManager
from chicken_disease_classification.components.data_validation import DataValidation

STAGE_NAME = "Data Ingestion stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_all_files_exist()
        except Exception as e:
            raise CustomException(e, sys)