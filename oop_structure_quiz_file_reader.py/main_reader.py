from core.utils import get_quiz_file_path
from features.random_quiz import random_quiz

def main():
    file_path = get_quiz_file_path()
    quiz = random_quiz(file_path)
    quiz.start()

if __name__ == "__main__":
    main()