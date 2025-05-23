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

        for index, q in enumerate(self.questions, 1):
            print(Style.BRIGHT + f"\n{'='*70}")
            print(Fore.CYAN + f"Question {index}: {q['question']}\n")
            for key, text in q['choices'].items():
                print(f"  {key}) {text}")

            print("\n" + "-" * 70)
            while True:
                answer = input(Fore.YELLOW + "Your answer (a/b/c/d): ").lower()
                if answer in ['a', 'b', 'c', 'd']:
                    break
                print(Fore.RED + "❌ Invalid choice. Please select a, b, c, or d.")

            if answer == q['correct']:
                print(Fore.GREEN + "✅ Correct!")
                score += 1
            else:
                correct_option = q['correct']
                print(Fore.RED + f"❌ Incorrect. The correct answer was '{q['choices'][correct_option]}'")

            sleep(1.5)
            clear_screen()