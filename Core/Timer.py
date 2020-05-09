import threading

from events import Events


class Timer:
    def __init__(self, delay):
        self.events = Events()
        self.delay = delay
        self.doRepeat_stop = threading.Event()

    def doRepeat(self, f_stop):
        self.events.on_change()
        if not f_stop.is_set():
            threading.Timer(self.delay, self.doRepeat, [self.doRepeat_stop]).start()

    def start(self):
        self.doRepeat(self.doRepeat_stop)
