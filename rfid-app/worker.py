import threading

class BackgroundWorker():
    def __init__(self):
        self.timer1 = 0
        self.timer2 = 0
        self.timer3 = 0

    def run(self):
        self.thr = threading.Timer(1, self.timer_loop)
#        self.timer_loop()
        self.update()
        self.thr.start()
        print "Start background worker"

    def update(self):
        pass

    def cancel(self):
        pass

    def timer_loop(self):
#        self.thr = threading.Timer(0.6, BackgroundWorker.timer_loop, [self])
#        self.thr.start()

        thr_count = threading.enumerate()
        print thr_count

        self.timer1 += 1
        if self.timer1 >= 5:
            self.timer1 = 0
            print "Timer 1 pass"

        self.timer2 += 1
        if self.timer2 >= 20:
            self.timer2 = 0
            print "Timer 2 pass"

        self.timer3 += 1
        if self.timer3 >= 60:
            self.timer3 = 0
            print "Timer 3 pass"

if __name__ == "__main__":
    backgroundWorker = BackgroundWorker()
    backgroundWorker.run()
