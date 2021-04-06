# -*- coding: utf-8 -*-

import time
import threading
import multiprocessing


class Threading():

    def __init__(self):
        self.vector_A = [10, 15, 20, 17]
        self.vector_B = []
        self.list_size = len(self.vector_A)
        self.thread_list = []
        self.thread_num = 4
        self.thread_task()

    def fatorial(self, n):
        fat = n
        for i in range(n-1, 1, -1):
            fat = fat * i
        return(fat)

    def calcFatorial(self, a_list, start, end):
        for item in a_list[start:end]:
            factorial = self.fatorial(item)
            self.vector_B.append(factorial)

    def thread_task(self):
        for i in range(self.thread_num):
            start = i * int(self.list_size/self.thread_num)
            end = (i + 1) * int(self.list_size/self.thread_num)
            t = threading.Thread(target=self.calcFatorial,
                                 args=(self.vector_A, start, end))
            t.start()
            self.thread_list.append(t)

        for t in self.thread_list:
            t.join()

        print(self.vector_B)

Threading()