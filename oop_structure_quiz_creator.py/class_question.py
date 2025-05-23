class Question:
    def __init__(self, question, choices, correct):
        self.question = question
        self.choices = choices
        self.correct = correct

    def to_text(self):
        text = f"question: {self.question} \n"
        for key in ['a', 'b', 'c', 'd']:
            text += f"{key}) {self.choices[key]}\n"
        text += f"Correct Answer: {self.correct}\n"
        text += "-" * 40 + "\n"
        return text