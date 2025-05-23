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
        
        clear_screen()
        print("\n" + "🎉 Welcome to the Random Quiz Challenge! 🎉".center(70))
        print("Answer the questions below and test your knowledge!\n".center(70))

        random.shuffle(self.questions)
        score = 0