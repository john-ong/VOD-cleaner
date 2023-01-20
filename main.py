import os
import time
import logging

folder_path = "FILE PATH"
age_limit = 180 # days

logging.basicConfig(filename='file_deletion.log', level=logging.INFO)

current_time = time.time()
deleted_count = 0

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        file_time = os.path.getmtime(file_path)
        if current_time - file_time > age_limit * 86400:
            os.remove(file_path)
            deleted_count += 1
            logging.info("Deleted file: %s", file_path)

logging.info("Deleted %d files", deleted_count)
