from resources.load import btc_threads
import threading

#start threads
for thread in btc_threads:
    thread.start()
