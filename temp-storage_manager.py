import os
import time
import platformdirs
from datetime import datetime, timedelta

folder_path = os.path.join(platformdirs.user_desktop_dir(), "temp-storage")

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

def clean_old_files():
    current_time = time.time()
    seconds_in_24hrs = 86400

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        try:
            creation_time = os.path.getctime(file_path)
            file_age = current_time - creation_time

            if file_age > seconds_in_24hrs:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    import shutil
                    shutil.rmtree(file_path)
                print(f"Deleted expired item: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

while True:
    clean_old_files()
    time.sleep(3600)