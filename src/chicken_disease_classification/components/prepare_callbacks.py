import os
import tensorflow as tf
import time
from chicken_disease_classification.entity.config_entity import PrepareCallbacksConfig
from chicken_disease_classification.utils.common import create_directories



class PrepareCallbacksTrainingPipeline:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    
    @property
    def _create_tb_callback(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_run_log_dir = os.path.join(self.config.tensorboard_root_log_dir, timestamp)
        tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=tb_run_log_dir)
        return tensorboard_callback
    
    @property
    def _create_checkpoint_callback(self):
        checkpoint_dir = os.path.dirname(self.config.checkpoint_model_filepath)
        create_directories([checkpoint_dir])
        checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True,
        )
        return checkpoint_callback
    
    def get_tb_ckpt_callbacks(self):
        tb_callback = self._create_tb_callback
        ckpt_callback = self._create_checkpoint_callback
        return [
            tb_callback, 
            ckpt_callback
        ]