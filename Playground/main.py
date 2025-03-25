class FileManager:
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


with FileManager('test.txt', 'w') as f:
    f.write('Text')
