#from __future__ import print_function


from threading import Timer

class RepeatingTimer():

    def __init__(self, interval, f):
        self.interval = interval
        self.f = f
        self.timer = None

    def callback(self):
        self.f()
        self.start()

    def cancel(self):
        self.timer.cancel()

    def start(self):
        self.timer = Timer(self.interval, self.callback)
        self.timer.start()