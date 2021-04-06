# -*- coding: utf-8 -*-
"""
/****************************** ASSESSMENT *********************************
*    Questao 06                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Desenvolvimento Python para Redes e             *
*                           Sistemas Operacionais                          *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_06.py                                   *
***************************************************************************/
"""
import socket
import os
import pickle
import errno
import time
from psutil._common import bytes2human


class Questao_06_Server():
    """ This is a TCP server program. """

    def __init__(self):
        """ Constructor """
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_host = socket.gethostname()
        self.door = 8881
        self.server_socket.bind((self.server_host, self.door))
        self.server_socket.listen()
        print('\nServidor de nome {} esperando conexão na porta {}'.format(
            self.server_host, self.door))

        while True:
            (socket_client, addr) = self.server_socket.accept()
            print("Conectado a:", str(addr))
            msg = socket_client.recv(2048)
            directory_name = msg.decode('ascii')
            
            client_list = self.process_data(directory_name)
            print('Requisitando informações...')
            msg = pickle.dumps(client_list)
            time.sleep(2)
            socket_client.send(msg)
            print('Informações enviadas!')
            
            socket_client.close()

    def process_data(self, directory):
        """ This function process the input data from init_class. """

        if os.path.exists(directory):
            self.list_dir = os.listdir(directory)
        else:
            print('Diretório não existe!')
        list_file = []
        for item in self.list_dir:
            if os.path.isfile(item):
                list_file.append(
                    [item, bytes2human(os.stat(item).st_size)])
            elif os.path.isdir(item):
                pass
            else:
                self.error = FileNotFoundError(errno.ENOENT, os.strerror(
                    errno.ENOENT), os.path.basename(item))
        return list_file

Questao_06_Server()
