from src.exception.exception import MyException
from src.logger.logging import logging
from src.entity.artifact_entity import ModelPusherArtifact,ModelTrainerArtifact,ModelEvaluationArtifact
from src.entity.config_entity import ModelEvaluationConfig,ModelPusherConfig
import os,sys
from src.utils.ml_utils.metric.classification_metric import get_classification_score
from src.utils.main_utils.utils import save_object,load_object,write_yaml_file
import shutil


class ModelPusher:

    def __init__(self,model_pusher_config:ModelPusherConfig, model_eval_artifact:ModelEvaluationArtifact):

        try:
            self.model_pusher_config = model_pusher_config
            self.model_eval_artifact = model_eval_artifact
        except  Exception as e:
            raise MyException(e, sys)
    

    def initiate_model_pusher(self,)->ModelPusherArtifact:
        try:
            trained_model_path = self.model_eval_artifact.trained_model_path
            
            #Creating model pusher dir to save model
            model_file_path = self.model_pusher_config.model_file_path
            os.makedirs(os.path.dirname(model_file_path),exist_ok=True)
            shutil.copy(src=trained_model_path, dst=model_file_path)

            #saved model dir
            saved_model_path = self.model_pusher_config.saved_model_path
            os.makedirs(os.path.dirname(saved_model_path),exist_ok=True)
            shutil.copy(src=trained_model_path, dst=saved_model_path)

            #prepare artifact
            model_pusher_artifact = ModelPusherArtifact(saved_model_path=saved_model_path, model_file_path=model_file_path)
            return model_pusher_artifact
        except  Exception as e:
            raise MyException(e, sys)