#Quiz creator class

import os
from class_question import Question
from question_saver import QuestionSaver

class QuizCreator:
    def __init__(self):
        self.file_path = os.path.join(os.path.expanduser("~"), "Desktop", "quiz.txt")
        self.saver = QuestionSaver(self.file_path)

    def get_question_from_user(self):
        print ("\nEnter your multiple choice question: ")
        question_text = input("Question: ")
        choices = {
            'a': input("Answer a: "),
            'b': input("Answer b: "),
            'c': input("Answer c: "),
            'd': input("Answer d: ")
        }

        while True:
            correct = input ("Which is the correct answer? (a/b/c/d): ").lower()
            if correct in choices:
                break
            print("Invalid input. Please enter one of a, b, c, or d. ")

        return Question(question_text, choices, correct)
    
    def run(self):
        while True:
            question = self.get_question_from_user()
            self.saver.save_question(question)

            while True:
                cont = input("Do you want to add another question? (yes/no): ").lower()
                if cont in ['yes', 'no']:
                    break
                print("Invalid input. Please type 'yes' or 'no'.")

            if cont == 'no':
                print("Exiting. Questions saved to", self.file_path)
                break


if __name__ == "__main__":
    creator = QuizCreator()
    creator.run()