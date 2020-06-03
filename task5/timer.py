import time


class Timer:
    def __init__(self):
        self.start_time = None
        self.stop_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.stop_time = time.time()

    @property
    def time_elapsed(self):
        return round((time.time() - self.start_time), 2)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        self.stop()