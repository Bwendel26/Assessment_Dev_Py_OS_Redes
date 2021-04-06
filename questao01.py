# -*- coding: utf-8 -*-

import psutil
import time
from psutil._common import bytes2human


class Questao_01():
    """
    This program gets the logged username.
    """

    def __init__(self):
        """ Constructor """
        self.info_dict = {}
        self.username = ''
        self.process_data()

    def init_class(self):
        """ This function receives the input data from users. """
        pass

    def process_data(self):
        """ This function process the input data from init_class. """

        for i in psutil.process_iter():
            if psutil.pid_exists(i.pid):
                self.info_dict[i.pid] = [
                    i.name(),
                    i.cpu_percent(),
                    round(i.memory_percent(), 2)
                ]
            else:
                pass
        return self.info_dict

    def print_result(self):
        """ This is a printer! It prints. """
        # info_dict = self.process_data()
        print('===' * 25, 'Questão 01'.center(75), '===' * 25, sep='\n')
        print('{}{:<7}{:<10}{:<10}{:<10}'.format(' '*2, 'PID',
                                                 'CPU %', 'MEM %', 'Nome'), '---' * 25, sep='\n')
        time.sleep(1)
        for pid, info_pid in self.info_dict.items():
            print('{}{:<7}{:<10}{:<10}{:<10}'.format(
                ' '*2, pid, info_pid[1], info_pid[2], info_pid[0]))
            time.sleep(0.1)


Questao_01().print_result()
