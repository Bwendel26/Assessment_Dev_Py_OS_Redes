# -*- coding: utf-8 -*-

import time


class Questao_05():
    """
    This program gets the logged username.
    """

    def __init__(self):
        """ Constructor """
        self.info_dict = {}
        self.a_list = list()
        self.b_list = list()
        self.list_sum = list()
        self.init_class()
        self.process_data()

    def init_class(self):
        """ This function receives the input data from users. """
        with open('a.txt', 'r', encoding='utf-8') as a_file:
            for item in a_file.readlines():
                a_list = item.split(' ')
        a_file.close()
        for _int in a_list:
            self.a_list.append(int(_int))

        with open('b.txt', 'r', encoding='utf-8') as b_file:
            for item in b_file.readlines():
                b_list = item.split(' ')
        b_file.close()
        for _int in b_list:
            self.b_list.append(int(_int))

    def process_data(self):
        """ This function process the input data from init_class. """

        len_a = len(self.a_list)
        len_b = len(self.b_list)
        dif = len_a - len_b

        if dif > 0:
            for i in range(0, abs(dif)):
                self.b_list.append(0)
        elif dif < 0:
            for i in range(0, abs(dif)):
                self.a_list.append(0)
        else:
            pass
        for a, b in zip(self.a_list, self.b_list):
            self.list_sum.append(sum([a, b]))

    def print_result(self):
        """ This is a printer! It prints. """
        print('===' * 25, 'Questão 05'.center(75), '===' * 25,
              'A soma dos números nos arquivos a.txt e b.txt é: ', sep='\n')
        for _sum in self.list_sum:
            print('{}{:<7}'.format(' '*2, _sum))
            time.sleep(0.5)


Questao_05().print_result()
