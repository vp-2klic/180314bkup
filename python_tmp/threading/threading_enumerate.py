import threading
import time
import logging
import random

def worker():
    """"thread worker function"""
#    t = threading.currentThread()
    pause = random.randint(1,5)
    logging.debug("Sleeping %s", pause)
    time.sleep(pause)
    logging.debug("Ending")
    return

logging.basicConfig(
                   level=logging.DEBUG, 
                   format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                   )
for i in range(3):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug("Joining %s", t.getName())
    t.join()
