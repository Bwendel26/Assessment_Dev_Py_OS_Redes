# -*- coding: utf-8 -*-
"""
/****************************** ASSESSMENT *********************************
*    Questao 09                                                            *
*        Aluno           : Francisco Alves Camello Neto                    *
*        Disciplina      : Desenvolvimento Python para Redes e             *
*                           Sistemas Operacionais                          *
*        Professor       : Thaís do Nascimento Viana                       *
*        Nome do arquivo : questao_09.py                                   *
***************************************************************************/
"""
import time
import random


class Sequencial():

    def __init__(self):
        print('===' * 25, 'Questão 09-a'.center(75), '===' * 25, sep='\n')
        self.vector_size = int(input("Entre com o tamanho do vetor: "))
        self.vector_A = []
        self.vector_B = []
        
    def fatorial(self, n):
        fat = n
        for i in range(n-1, 1, -1):
            fat = fat * i
        return(fat)

    def calc_factorial(self):

        self.start_time = float(time.time())

        for i in range(self.vector_size):
            self.vector_A.append(random.randint(0, self.vector_size))

        for item in self.vector_A:
            sq_factor = self.fatorial(item)
            self.vector_B.append(sq_factor)

        self.end_time = float(time.time())

    def print_result(self):
        """ This is a printer! It prints. """
        self.calc_factorial()
        print('{}Tempo de processamento sequencial: {}'.format(' '*2, self.end_time - self.start_time))
        print('---' * 25, 'Aluno: Francisco Camello'.rjust(75), sep="\n")


Sequencial().print_result()