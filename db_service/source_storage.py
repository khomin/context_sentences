import os


class SourceStorage:
    def __init__(self):
        list_of_all = os.listdir("./data_sources")
        self.list_of_files = []

        for i in list_of_all:
            if (not i.__contains__('.DS_Store')):
                self.list_of_files.append(i)

    def get_size(self):
        return len(self.list_of_files)

    def get_items(self):
        return self.list_of_files
