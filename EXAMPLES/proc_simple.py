#!/usr/bin/env python
from multiprocessing import Process
import random
import time


class SimpleProcess(Process):
    def __init__(self, num):
        super().__init__()  # <1>
        self._threadnum = num

    def run(self):  # <2>
        time.sleep(random.randint(1, 3))
        print("Hello from process {}".format(self._threadnum))

if __name__ == '__main__':

    for i in range(16):
        t = SimpleProcess(i)  # <3>
        t.start()  # <4>

    print("Done.")
