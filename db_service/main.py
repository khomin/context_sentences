from fill_db import Fill_DB

from source_storage import SourceStorage

print('fill database')

print('getting list of urls to scan')
source_storage = SourceStorage()
sources_len = source_storage.get_size()

if sources_len == 0:
    print("sources list is empty\nPlease check the book directory")
else:
    print("sources_len size: " + str(sources_len))

    fill_db = Fill_DB()
    number_of_lines = fill_db.start(source_storage)

    print("fill database done, number of lines: " + str(number_of_lines))
