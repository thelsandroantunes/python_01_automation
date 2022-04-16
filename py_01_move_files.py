from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import json
import os
import time
import shutil


class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(folder_to_track):
            file_folder = os.path.join(folder_to_track, file)
            shutil.move(file_folder, destination_folder)


folder_to_track = "C://Users//thels//Downloads//teste"
destination_folder = "C://Users//thels//OneDrive//Documentos"

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
