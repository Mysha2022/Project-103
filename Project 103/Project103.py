import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "Downloads"


# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
       print(f"Hey,{event.src_path} has been created")
    
    def on_deleted(self, event):
       print(f"Opps, someone deleted {event.src_path}")

    def on_modified(self, event):
       print(f"Hey there, {event.src_path} has been modified")

    def on_moved(self, event):
       print(f"Someone moved {event.src_path} to {event.dest_path}")



# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt:
    print("Stop")
    observer.stop()
        

    