class FileManagement:
    def __init__(self, name):
        self.file = open(name, "a")

    def __enter__(self):
        return self.file

    def file_write(self, file_text):
        self.file.write(file_text)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
