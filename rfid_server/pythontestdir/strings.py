#! /usr/bin/python2

import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG, \
                    format='(%(threadName)-10s) %(message)s', \
                    )

def thread1():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exitting')

t = threading.Thread(name='Task 1', target=thread1)
t.setDaemon(True)

def thread2():
    logging.debug('Starting')
#    time.sleep(2)
    logging.debug('Exitting')

w = threading.Thread(name='Task 2', target=thread2)
# w2 = threading.Thread(target=thread2)

t.start()
w.start()

t.join(4)
print 't.isAlive()', t.isAlive()
w.join()
