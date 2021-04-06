# -*- coding: utf-8 -*-

import time
import threading
import multiprocessing


class Sequencial():
    vector_A = [10, 15]
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

Sequencial().print()