import threading
import time
import logging

def worker():
    """"thread worker function"""
    logging.debug("Starting")
    time.sleep(0.5)
    logging.debug("Stopping")

def my_service():
    """"thread service function"""
    logging.debug("Starting")
    time.sleep(0.3)
    logging.debug("Stopping")

logging.basicConfig(
                   level=logging.DEBUG, 
                   format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                   )

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)

w.start()
w2.start()
t.start()
