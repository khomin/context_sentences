import os

from tqdm import tqdm

from db import Db


class FillDb:
    def __init__(self):
        self.db = Db()
        self.db.create_connection(os.getcwd() + '/sqlite.db')

    def start(self, source_storage):
        entire = []
        items = source_storage.getItems()

        for it in items:
            f = open(os.getcwd() + '/data_sources/' + it, "r", errors='replace')
            raw_entire = f.read().splitlines()

            last_line_char = None
            last_line = ''

            for line in raw_entire:
                if len(line) != 0:
                    if last_line_char is None:
                        entire.append(line)
                        last_line_char = line[-1]
                    else:
                        if line[0].islower():
                            it = line
                            entire[-1] = entire[-1] + ' ' + it
                            last_line_char = it[-1]
                        else:
                            entire.append(line)
                            last_line_char = it[-1]
                last_line = line

        with open(os.getcwd() + '/summary_out.txt', "w") as txt_file:
            txt_file.truncate(0)

            for line in entire:
                sub_line = line.split('.')
                if len(sub_line) > 1:
                    for s_line in sub_line:
                        if len(s_line) > 0:
                            if s_line[0] == ' ':
                                s_line = s_line[1:]
                            txt_file.write(s_line + '\n')
                else:
                    if line[0] == ' ':
                        line = line[1:]
                    txt_file.write(line + '\n')

        if self.db.open_connection(os.getcwd() + '/sqlite.db'):
            try:
                for it_en in tqdm(entire):
                    self.db.insertTextSentence(it_en)
                print('\n')
            finally:
                self.db.close_connection()

        return len(entire)
