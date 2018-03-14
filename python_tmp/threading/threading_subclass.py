import threading
import time
import logging

logging.basicConfig(
                   level=logging.DEBUG, 
                   format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                   )

class myThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group=group, target=target, name=name, verbose=verbose)
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        logging.debug("Running with %s and %s", self.args, self.kwargs)
        return

for i in range(5):
    t = myThread(args=(i,), kwargs={'a':'A', 'b':'B'})
    t.start()
