import os
from colorama import Fore
from abc import ABC, abstractmethod

class BaseQuiz(ABC):
    def __init__(self, filename):
        self.filename = filename
        self.questions = self.load_questions()

        def load_questions(self):
            if not os.path.exists(self.filename):
                print(Fore.RED +  "⚠️ No quiz file found.")
                return[]
            
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read().strip()

            raw_questions = content.split("-" * 40)
            questions = []

            for raw in raw_questions:
                lines = [line.strip() for line in raw.strip().split("\n")]
                if len(lines) < 6:
                    continue

                question = lines[0].replace("Question: ", "")
            choices = {
                'a': lines[1].replace("a) ", ""),
                'b': lines[2].replace("b) ", ""),
                'c': lines[3].replace("c) ", ""),
                'd': lines[4].replace("d) ", "")
            }
            correct = lines[5].replace("Correct Answer: ", "").lower()

            questions.append({
                'question': question,
                'choices': choices,
                'correct': correct
            })

        return questions