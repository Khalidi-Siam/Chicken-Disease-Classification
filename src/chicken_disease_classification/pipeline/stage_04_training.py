import sys
from chicken_disease_classification.exception import CustomException
from chicken_disease_classification.config.configuration import ConfigurationManager
from chicken_disease_classification.components.prepare_callbacks import PrepareCallbacksTrainingPipeline
from chicken_disease_classification.components.training import Training
from chicken_disease_classification.logger import logging


STAGE_NAME = "Model Training stage"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            prepare_callbacks_config = config.get_prepare_callbacks_config()
            prepare_callbacks = PrepareCallbacksTrainingPipeline(config=prepare_callbacks_config)
            callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train(
                callbacks_list=callback_list
            )
            
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    try:
        logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        training = ModelTrainingPipeline()
        training.main()
        logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
    except Exception as e:
        raise CustomException(e, sys)
