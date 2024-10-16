import time
import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, file_to_watch, command):
        self.file_to_watch = file_to_watch
        self.command = command

    def on_modified(self, event):
        # Check if the modified file is the one we're watching
        file_to_watch = os.path.realpath(self.file_to_watch)
        src_path = os.path.realpath(event.src_path)
        if src_path == file_to_watch:
            print(f"{self.file_to_watch} has been modified. Executing command...")
            subprocess.run(self.command, shell=True)

def watch_file(file_path, command):
    event_handler = FileChangeHandler(file_path, command)
    observer = Observer()
    folder_to_watch = os.path.dirname(file_path)
    observer.schedule(event_handler, path=folder_to_watch, recursive=False)
    observer.start()
    print(f"Watching folder...:{folder_to_watch}")
    
    try:
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Use it to watch a specific file and execute a command
file_path = "./hfsl.py"
command = "C:\\Users\\naive\\er-level-souls-curve\\venv\\Scripts\\python.exe hfsl.py"    # Replace with the command to execute when the file changes
watch_file(file_path, command)
