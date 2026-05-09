import sys
from chicken_disease_classification.config.configuration import ConfigurationManager
from chicken_disease_classification.components.data_ingestion import DataIngestion
from chicken_disease_classification.exception import CustomException


STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise CustomException(e, sys)