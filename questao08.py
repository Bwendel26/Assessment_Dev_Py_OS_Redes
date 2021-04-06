# -*- coding: utf-8 -*-

import psutil
import time
from psutil._common import bytes2human
import threading

class Sequencial():
    vector_A = [10,15]
    vector_B = []

    def fatorial(self, n):
        fat = n
        for i in range(n-1, 1, -1):
            fat = fat * i
        return(fat)

    def print(self):
        for item in self.vector_A:
            sq_factor = self.fatorial(item)
            self.vector_B.append(sq_factor)
        print(self.vector_B)

class Threading():
    vector_A = [10,15]
    vector_B = []

    def fatorial(self, n):
        fat = n
        for i in range(n-1, 1, -1):
            fat = fat * i
        return(fat)
    t0 = threading.Thread(target=fatorial, args=(vector_A,))
    t0.start()
    print(t0)
    def result(self, vector):
        for item in self.vector_A:
            th_factor = self.fatorial(item)
            vector.append(th_factor)
        print(vector)
    t1 = threading.Thread(target=result, args=(vector_B,))
    t1.start()
    print(t1)

class Multiprocessing():
    vector_A = [10,15]
    vector_B = []

    def fatorial(self, n):
        fat = n
        for i in range(n-1, 1, -1):
            fat = fat * i
        return(fat)

    def print(self):
        for item in self.vector_A:
            mt_factor = self.fatorial(item)
            self.vector_B.append(mt_factor)
        print(self.vector_B)


Threading()