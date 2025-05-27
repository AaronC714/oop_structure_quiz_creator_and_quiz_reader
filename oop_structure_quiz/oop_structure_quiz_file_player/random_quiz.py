import random
from time import sleep
from colorama import Fore, Style
from base_quiz import BaseQuiz
from core_and_utilities import clear_screen

class random_quiz(BaseQuiz):
    def start(self):
        if not self.questions:
            print ("No questions found for the quiz.")
            return
        
        clear_screen()
        print("\n" + "🎉 Welcome to the Random Quiz Challenge! 🎉".center(70))
        print("Answer the questions below and test your knowledge!\n".center(70))

        random.shuffle(self.questions)
        score = 0

        for index, question_text in enumerate(self.questions, 1):
            print(Style.BRIGHT + f"\n{'='*70}")
            print(Fore.CYAN + f"Question {index}: {question_text['question']}\n")
            for key, text in question_text['choices'].items():
                print(f"  {key}) {text}")

            print("\n" + "-" * 70)
            while True:
                answer = input(Fore.YELLOW + "Your answer (a/b/c/d): ").lower()
                if answer in ['a', 'b', 'c', 'd']:
                    break
                print(Fore.RED + "❌ Invalid choice. Please select a, b, c, or d.")

            if answer == question_text['correct']:
                print(Fore.GREEN + "✅ Correct!")
                score += 1
            else:
                correct_option = question_text['correct']
                print(Fore.RED + f"❌ Incorrect. The correct answer was '{question_text['choices'][correct_option]}'")

            sleep(1.5)
            clear_screen()

        print("\n" + "=" * 70)
        print(Fore.MAGENTA + f"🏁 Quiz Over! You scored {score} out of {len(self.questions)}.\n")
        if score == len(self.questions):
            print(Fore.GREEN + "🌟 Perfect score! You're a quiz master!")
        elif score >= len(self.questions) // 2:
            print(Fore.CYAN + "💡 Good job! Keep practicing.")
        else:
            print(Fore.YELLOW + "📚 Keep studying and try again!")
        print("=" * 70 + "\n")