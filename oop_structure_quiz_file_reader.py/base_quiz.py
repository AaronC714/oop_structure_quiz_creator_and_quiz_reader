import os
from colorama import Fore
from abc import ABC, abstractmethod

class BaseQuiz(ABC):
    def __init__(self, filename):
        self.filename = filename
        self.questions = self.load_questions()

        def laod_questions(self):
            if not os.path.exists(self.filename):
                print(Fore.RED +  "⚠️ No quiz file found.")
                return[]