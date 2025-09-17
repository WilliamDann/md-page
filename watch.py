import config
import time
import md

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            print(f"Directory created: {event.src_path}")
        else:
            print(f"File created: {event.src_path}")
        md.processDir(config.ARGS['input'], config.ARGS['output'])

    def on_deleted(self, event):
        if event.is_directory:
            print(f"Directory deleted: {event.src_path}")
        else:
            print(f"File deleted: {event.src_path}")
        md.processDir(config.ARGS['input'], config.ARGS['output'])

    def on_modified(self, event):
        if event.is_directory:
            print(f"Directory modified: {event.src_path}")
        else:
            print(f"File modified: {event.src_path}")
        md.processDir(config.ARGS['input'], config.ARGS['output'])
    
    def on_moved(self, event):
        if event.is_directory:
            print(f"Directory moved from {event.src_path} to {event.dest_path}")
        else:
            print(f"File moved from {event.src_path} to {event.dest_path}")
        md.processDir(config.ARGS['input'], config.ARGS['output'])

# watch mode
def watch():
    print(" - Starting watch mode...")
    print("   Ctrl + C to exit")

    md.processDir(config.ARGS['input'], config.ARGS['output'])
    
    path_to_watch = config.ARGS['input']
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print()

    observer.join()
