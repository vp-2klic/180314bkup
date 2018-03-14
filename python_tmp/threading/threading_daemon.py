import threading
import time
import logging

def daemon():
    """"thread daemon function"""
    logging.debug("Starting")
    time.sleep(0.5)
    logging.debug("Stopping")

def non_daemon():
    """"thread non-daemon function"""
    logging.debug("Starting")
    time.sleep(0.3)
    logging.debug("Stopping")

logging.basicConfig(
                   level=logging.DEBUG, 
                   format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                   )

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join(0.4)
print "d.isAlive()", d.isAlive()
t.join()
