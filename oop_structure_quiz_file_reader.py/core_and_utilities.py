import os
from colorama import init

init (autoreset=True)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def get_quiz_file_path():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    return os.path.join(desktop_path, "quiz.txt")