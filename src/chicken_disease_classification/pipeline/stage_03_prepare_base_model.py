import sys
from chicken_disease_classification.exception import CustomException
from chicken_disease_classification.config.configuration import ConfigurationManager
from chicken_disease_classification.components.prepare_base_model import PrepareBaseModel

STAGE_NAME = "Prepare Base Model stage"



class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise CustomException(e, sys)