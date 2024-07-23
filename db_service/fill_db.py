import os
import re
from tqdm import tqdm
from db import Db
import nltk.data

class FillDb:
    def __init__(self):
        self.db = Db()
        self.db.create_connection(os.getcwd() + '/sqlite.db')

    def start(self, source_storage):
        entire = []
        items = source_storage.get_items()
        for it in items:
            f = open(os.getcwd() + '/data_sources/' + it, "r", errors='replace')
            raw = f.read()
            # raw_entire = re.split('[?.,]', raw)
            raw_entire = raw.splitlines()


            if True: # self.__containsKeyWords(raw_entire):
                print("this book contains keywords: " + it)
                entire = self.__format2(raw_entire, raw)
                # entire.append(formatted)
                # formatted = self.__format_new_lines(raw_entire)
                # entire.append(self.__split_by_punctuation(formatted))

        with open(os.getcwd() + '/summary_out.txt', "w") as echo_file:
            echo_file.truncate(0)

            # raw_entire = re.split('[?.,]', raw)

            for line in entire:
                line_split = re.split('[?.!;:\n]', line)
                for sub_line in line_split:
                    hasChanges = True
                    # remove two space
                    sub_line = sub_line.replace('  ', ' ')
                    while hasChanges:
                        hasChanges = False
                        try:
                            if sub_line.index("How so") >= 0:
                                print("")
                        # ’ ‘
                        except:
                            None
                        if sub_line.startswith('‘'):
                            sub_line = sub_line[1:]
                            hasChanges = True
                        if sub_line.startswith('’'):
                            sub_line = sub_line[1:]
                            hasChanges = True
                        if sub_line.endswith('‘'):
                            sub_line = sub_line[:-1]
                            hasChanges = True
                        if sub_line.endswith('’'):
                            sub_line = sub_line[:-1]
                            hasChanges = True
                        if sub_line.startswith(' '):
                            sub_line = sub_line[1:]
                            hasChanges = True
                    # write
                    echo_file.write(sub_line + '\n')

        if self.db.open_connection(os.getcwd() + '/sqlite.db'):
            try:
                for it_line in tqdm(entire):
                    for it_line_one in it_line:
                        self.db.insert_text_sentence(it_line_one)
                print('\n')
            finally:
                self.db.close_connection()

        return len(entire)

    def __format2(self, input, input_raw):
        # 1 remove “”
        # 2 remove all lines with 2 words between space
        # remove all starting with "Copyright"
        # nltk.download('punkt')
        # sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
        # parsed = sent_detector.tokenize(input_raw)#''.join(input))
        # print('\n-----\n'.join(parsed))

        hasEnd = False
        skipLine = False
        entire = []
        prev_line = ''
        for i in range(0, len(input)): 
            line = input[i]
            
            line = line.replace('“', '')
            line = line.replace('”', '')
            # line = line.replace("‘", '')
            # line = line.replace("’", '')
            line = line.replace('...', ' ')
            line = line.replace('.', '\n')

            # if line.isupper():
            #     hasEnd = True
            #     skipLine = True
            #     continue

            # count = len(line.split())
            # if count <= 3 and:
            #     hasEnd = True
            #     skipLine = True
            #     continue

            if line == "":
                continue

            if line.startswith('Chapter'):
                hasEnd = True
                skipLine = True
                continue

            # if hasEnd == False:
                # entire.append(line)
            
            if prev_line != '':
                # if prev_line.endswith('.') or prev_line.endswith(',') \
                #     or prev_line.endswith(';') or prev_line.endswith('?') \
                #     or prev_line.endswith('!'):
                #     entire.append('\n' + line)
                # else:
                    if len(entire) > 0:
                        entire[len(entire)-1] += " " + line
                    else:
                        entire.append(line)
            else:
                entire.append(line)


            # if line.endswith('.') or line.endswith(',') or line.endswith(';') or line.endswith('?') or line.endswith('!'):
            #     hasEnd = True
            #     entire.append(line)
            # else:
            #     next_line = input[i+1]
            #     if next_line != '' and next_line[0].islower():
            #         entire.append(line)
            #     hasEnd = False

            prev_line = line
        
        # for line in input:
        #     if len(line) != 0:
        #         if last_line_char is None:
        #             entire.append(line)
        #             last_line_char = line[-1]
        #         else:
        #             it = line[0]
        #             if line[0].islower():
        #                 entire[-1] = entire[-1] + ' ' + it
        #                 last_line_char = it[-1]
        #             else:
        #                 entire.append(line)
        #                 last_line_char = it[-1]
        return entire

    def __format_new_lines(self, input):
        last_line_char = None
        entire = []

        for line in input:
            if len(line) != 0:
                if last_line_char is None:
                    entire.append(line)
                    last_line_char = line[-1]
                else:
                    it = line[0]
                    if line[0].islower():
                        entire[-1] = entire[-1] + ' ' + it
                        last_line_char = it[-1]
                    else:
                        entire.append(line)
                        last_line_char = it[-1]
        return entire

    def __split_by_punctuation(self, input):
        entire = []

        for line in input:
            line = re.split('[;:_!?.]', line)
            for line_one in line:
                entire.append(line_one)
        return entire
    
    def __containsKeyWords(self, input):
        foundCnt = 0
        l = ["haggard", "erratic", "moat", "arduous"]
        for it in l:
            for it2 in input:
                try:
                    index = it2.index(it)
                    foundCnt += 1
                except Exception  as e:
                    None #print(e)
        return foundCnt != 0