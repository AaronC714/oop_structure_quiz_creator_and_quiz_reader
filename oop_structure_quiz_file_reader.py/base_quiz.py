import os
from colorama import Fore
from abc import ABC, abstractmethod

class BaseQuiz(ABC):
    def __init__(self, filename):
        self.filename = filename
        self.questions = self.load_questions()