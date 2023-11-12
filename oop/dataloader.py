class DataLoader:
    file_path = None
    is_directory = False
    is_loaded = None

    def __init__(self, path, isdirectory):
        self.file_path = path
        self.is_directory = isdirectory

    def printme(self):
        print(f"path is {self.file_path} isdirectory {self.is_directory}")


'''
data = DataLoader(path="c:\dataset", isdirectory=True)
data.printme()
print(data.is_directory)
print(data.file_path)
print(data.is_loaded)

'''

