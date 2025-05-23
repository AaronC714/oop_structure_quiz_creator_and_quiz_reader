#Quiz creator class

import os
from models.question import Question
from io.question_saver import Question_saver

class QuizCreator:
    def __inti__(self):
        self.file_path = os.path.join(os.path.expanduser("~"), "Desktop", "quiz.txt")
        self.saver = QuestionSaver(self.file_path)