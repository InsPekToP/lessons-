#2main11_2s.py
#НИХРЕНА НЕ ПОЛУЧИЛОСЬ.НАДо РАЗОБРАТьСЯ
#Прога для быстрого перемешения из папки в папку
#pip install watchdog

from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler, FileSystemEvent  # непонятно нахуя это сделали

class Handler(FileSystemEventHandler):
    def on_modified(self,event):
        for filename in os.listdir(folder_track):
            extention = filename.split(".")
            if len(extention) > 1 and (extension[1].lower() == "jpg" or extension[1].lower() == "png" or extension[1].lower() == "svg"):
                file = folder_track + "/" + filename
                new_path = folder_dest + "/" + filename
                os.rename(file,new_path)

folder_track = 'E:\Downloads'
folder_desk = 'E:\Курсы\Python_ITproger\Видео_уроки\2й_модуль'

hadle = Handler()
observer = Observer()
observer.schedule(hadle,folder_track,recursive= True)
observer.start()

try: #задержка
    while(True):
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
