# -*- coding: utf-8 -*-
"""
/****************************** ASSESSMENT *********************************
*    Questao 03                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Desenvolvimento Python para Redes e             *
*                           Sistemas Operacionais                          *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_03.py                                   *
***************************************************************************/
"""
import os
from pathlib import Path as path
from psutil._common import bytes2human
import errno


class Questao_03():
    """
    This program lists the files in a given directory.
    """

    def __init__(self):
        """ Constructor """
        self.search_path = path.home() / 'Documents'
        self.error = ''
        self.list_dir = list()
        self.list_file = list()
        print('===' * 25, 'Questão 03'.center(75), '===' * 25, sep='\n')
        self.init_class()
        self.process_data()

    def init_class(self):
        """ This function receives the input data from users. """

        if os.path.exists(self.search_path):
            self.list_dir = os.listdir(self.search_path)
        else:
            self.search_path = input(str('Digite o caminho de um diretório: '))
            os.chdir(self.search_path)
            self.list_dir = os.listdir(os.chdir(self.search_path))

    def process_data(self):
        """ This function process the input data from init_class. """
        for item in self.list_dir:
            if os.path.isfile(os.path.join(self.search_path, item)):
                self.list_file.append({
                    'name': item,
                    'size': os.stat(os.path.join(self.search_path, item)).st_size
                })
                self.list_file.sort(key=lambda x: x['size'], reverse=True)
            elif os.path.isdir(os.path.join(self.search_path, item)):
                pass
            else:
                self.error = FileNotFoundError(errno.ENOENT, os.strerror(
                    errno.ENOENT), os.path.basename(item))
        with open('questao03.txt', 'w') as _file:
            _file.write(str(self.list_file))

    def print_result(self):
        """ This is a printer! It prints. """
        if self.error:
            print(self.error,
                  '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")
        else:
            print('Conteúdo do diretório: \n {}'.format(os.path.abspath(self.search_path)),
                  '{} {:<10} {:^10}'.format(' '*2, 'Tamanho', 'Arquivo'), sep="\n")
            for _file in self.list_file:
                print('{} {:<10} {:^10}'.format(
                    ' '*2, bytes2human(_file['size']), _file['name']))
        print('---' * 25, 'O arquivo questao03.txt foi criado com sucesso!',
              '---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Questao_03().print_result()
