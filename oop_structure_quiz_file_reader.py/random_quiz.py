import random
from time import sleep
from colorama import Fore, Style
from base_quiz import BaseQuiz
from core_and_utilities import clear_screen

class RandomQuiz(BaseQuiz):
    def start(self):
        if not self.questions:
            print ("No questions found for the quiz.")
            return