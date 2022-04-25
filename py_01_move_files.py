from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time
import shutil

# ========== Function Select extension files Start========== #


class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(folder_to_track):
            if file.endswith('.pdf') or file.endswith('.doc') or file.endswith('.txt') or file.endswith('.ppt'):
                os.rename(folder_to_track+'//'+file, pdf_directory+'//'+file)
            elif file.endswith('.jpg') or file.endswith('.JPG') or file.endswith('.png') or file.endswith('.PNG') or file.endswith('.jpeg') or file.endswith('.svg') or file.endswith('.eps'):
                os.rename(folder_to_track+'//'+file, img_directory+'//'+file)
            elif file.endswith('.mp4') or file.endswith('.avi') or file.endswith('.vob') or file.endswith('.flv') or file.endswith('.mpeg') or file.endswith('.m4v'):
                os.rename(folder_to_track+'//'+file, mp4_directory+'//'+file)
            elif file.endswith('.epub') or file.endswith('.mobi'):
                os.rename(folder_to_track+'//'+file, book_directory+'//'+file)
            elif file.endswith('.exe'):
                shutil.move(folder_to_track+'//'+file, exe_directory+'//'+file)
            else:
                print('Other file format: ' + file)

            #file_folder = os.path.join(folder_to_track, file)
            #shutil.move(file_folder, destination_folder)
# ========== Function Select extension files End========== #


# ========== Folder Original Start ========== #
folder_to_track = "C://Users//thels//Downloads"
# ========== Folder Original End ========== #

# ========== Moving the files Start ========== #
pdf_directory = "C://Users//thels//OneDrive//Documentos"
img_directory = "C://Users//thels//OneDrive//Imagens"
mp4_directory = "C://Users//thels//Videos"
book_directory = "C://Users//thels//Livros"
other_directory = "C://Users//thels//Others"

exe_directory = "C://Users//thels//Programs"
code_directory = "C://Users//thels//Code"
# ========== Moving the files End ========== #

# ========== Event Start ========== #
event_handler = FileHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

# ========== Event End ========== #
