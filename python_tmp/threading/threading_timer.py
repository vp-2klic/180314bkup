import threading
import time
import logging

logging.basicConfig(
                   level=logging.DEBUG, 
                   format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                   )

def delayed():
    """"thread delay function"""
    logging.debug("Worker is Running")
    return

t1=threading.Timer(3, delayed)
t1.setName('t1')
t2=threading.Timer(3, delayed)
t2.setName('t2')

logging.debug("Starting Timers")
t1.start()
t2.start()

logging.debug("Waiting before canceling %s", t2.getName())
time.sleep(4)
logging.debug("Canceling %s", t2.getName())
t2.cancel()
logging.debug("Done")
