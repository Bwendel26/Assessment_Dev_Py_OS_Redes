# -*- coding: utf-8 -*-

import socket
import os
import pickle
import time

class Questao_06_Client():
    """ This is a TCP client program. """

    def __init__(self):
        """ Constructor """
        os.chdir(os.path.dirname(__file__))
        self.cwd = os.getcwd()
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_host = socket.gethostname()
        self.door = 8881
        print('===' * 25, 'Questão 06'.center(75), '===' * 25, sep='\n')
        self.directory_name = input('Entre com o nome do diretório: ')

        try:
            self.client_socket.connect((self.client_host, self.door))
            self.client_socket.send(self.directory_name.encode('ascii'))
            msg = self.client_socket.recv(4096)
            l_msg = pickle.loads(msg)
            self.print_result(l_msg)
            
        except Exception as err:
            print(str(err))
            self.client_socket.close()
        input("Pressione qualquer tecla para sair...")

    def print_result(self, list_file):
        """ This is a printer! It prints. """
        print('---' * 25, 'Informações recebidas!', '---' * 25, sep='\n')
        time.sleep(2)
        print('Conteúdo do diretório: \n {}'.format(os.path.abspath(self.directory_name)),
                '\t {:<15} {:^10}'.format('Arquivo', 'Tamanho'), sep="\n")
        for _file in list_file:
            print('\t {:<15} {:^10}'.format(_file[0], _file[1]))

Questao_06_Client()
