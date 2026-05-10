import sys
from chicken_disease_classification.exception import CustomException
from chicken_disease_classification.config.configuration import ConfigurationManager
from chicken_disease_classification.components.evaluation import Evaluation
from chicken_disease_classification.logger import logging


STAGE_NAME = "Model Evaluation stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(eval_config)
            evaluation.evaluation()
            evaluation.save_score()

        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    try:
        logging.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        evaluation = EvaluationPipeline()
        evaluation.main()
        logging.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
    except Exception as e:
        raise CustomException(e, sys)