import os
import re
from tqdm import tqdm
from db import Db
import nltk.data

class Fill_DB:
    def __init__(self):
        self.db = Db()
        self.db.create_connection(os.getcwd() + '/sqlite.db')

    def start(self, source_storage):
        entire = []
        items = source_storage.get_items()
        for it in items:
            f = open(os.getcwd() + '/data_sources/' + it, "r", errors='replace')
            raw = f.read()
            raw_entire = raw.splitlines()

            if self.__contains_keys(raw_entire):
                print("this book contains keywords: " + it)
                entire = self.__format(raw_entire)

                self.__write_summary(entire)

                if self.db.open_connection(os.getcwd() + '/sqlite.db'):
                    try:
                        for it_line in tqdm(entire):
                            for it_line_one in it_line:
                                self.db.insert_text_sentence(it_line_one)
                        print('\n')
                    finally:
                        self.db.close_connection()

        return len(entire)

    def __format(self, input):
        entire = []
        entire_temp = []
        prev_line = ''
        for i in range(0, len(input)): 
            skip_line = False
            line = input[i]
            line = line.replace('“', '')
            line = line.replace('”', '')
            line = line.replace('...', ' ')
            line = line.replace('.', '\n')

            # too short
            count = len(line.split())
            if count <= 2:
                skip_line = True

            if line == "":
                skip_line = True

            if line.startswith('Chapter'):
                skip_line = True

            ignore = ['https','http', 'www', '.com']
            for i in ignore:
                try:
                    if line.index(i) >= 0:
                        skip_line = True
                except Exception  as e:
                    None
            
            if skip_line:
                continue

            if prev_line != '':
                if len(entire_temp) > 0:
                    entire_temp[len(entire_temp)-1] += " " + line
                else:
                    entire_temp.append(line)
            else:
                entire_temp.append(line)

            prev_line = line

        for line in entire_temp:
                line = line.replace('? ', '?\n')
                line = line.replace('! ', '!\n')
                line_split = re.split('[\n]', line)
                for sub_line in line_split:
                    has_changes = True
                    sub_line = sub_line.replace('  ', ' ')
                    while has_changes:
                        has_changes = False
                        if sub_line.startswith('‘'):
                            sub_line = sub_line[1:]
                            has_changes = True
                        if sub_line.startswith('’'):
                            sub_line = sub_line[1:]
                            has_changes = True
                        if sub_line.endswith('‘'):
                            sub_line = sub_line[:-1]
                            has_changes = True
                        if sub_line.endswith('’'):
                            sub_line = sub_line[:-1]
                            has_changes = True
                        if sub_line.startswith(' '):
                            sub_line = sub_line[1:]
                            has_changes = True

                    entire.append(sub_line)
        
        return entire
    
    def __contains_keys(self, input):
        found_cnt = 0
        l = ["haggard", "erratic", "moat", "arduous"]
        for it in l:
            for it2 in input:
                try:
                    it2.index(it)
                    found_cnt += 1
                except Exception  as e:
                    None
        return found_cnt != 0
    
    def __write_summary(self, entire):
        with open(os.getcwd() + '/summary_out.txt', "w") as echo_file:
            echo_file.truncate(0)
            for line in entire:
                echo_file.write(line + '\n')