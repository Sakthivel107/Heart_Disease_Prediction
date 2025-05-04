import os
import sys

from src.exception.exception import MyException
from src.logger.logging import logging

from src.pipeline.training_pipeline import TrainingPipeline

def start_training():
    try:
        model_training = TrainingPipeline()
        model_training.run_pipeline()
    except Exception as e:
        raise MyException(e,sys)
    

if __name__=='__main__':
    start_training()