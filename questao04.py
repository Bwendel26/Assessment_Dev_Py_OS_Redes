# -*- coding: utf-8 -*-

import psutil
import time
from psutil._common import bytes2human


class Questao_04():
    """
    This program gets the logged username.
    """

    def __init__(self):
        """ Constructor """
        self.line_file_list = list()
        print('===' * 25, 'Questão 04'.center(75), '===' * 25, sep='\n')
        self.init_class()
        self.process_data()

    def init_class(self):
        """ This function receives the input data from users. """
        pass

    def process_data(self):
        """ This function process the input data from init_class. """

        with open('arquivo.txt', 'r', encoding='utf-8', newline='\r\n') as _file:
            for line in _file:
                res = line[::-1].strip()
                self.line_file_list.append(res)
        self.line_file_list.sort(reverse=True)
        # print(self.line_file_list)
        return self.line_file_list

    def print_result(self):
        """ This is a printer! It prints. """
        for item in self.line_file_list:
            print(item)


Questao_04().print_result()
