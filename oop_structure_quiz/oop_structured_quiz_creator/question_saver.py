from .file_writer import FileWriter

class QuestionSaver(FileWriter):
    def save_question(self, question):
        self.write(question.to_text())