class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def write(self, text):
        with open(self.filename, "a") as file:
            file.write(text)