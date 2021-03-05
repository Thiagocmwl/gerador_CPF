"""
Autor: Thiago Silva Costa

Data: 04/03/2021

Objetivo: Gerar CPF aleatório
"""

from random import randint
import tkinter
from tkinter import messagebox

cpf = str(randint(100000000, 999999999))

# Gerar primeiro dígito
i = 10
soma = 0
for x in range(9):
    soma += int(cpf[x]) * i
    i -= 1

if 11 - (soma % 11) > 9:
    digito_1 = 0
else:
    digito_1 = 11 - (soma % 11)
cpf += str(digito_1)

# Gerar segundo dígito
i = 11
soma = 0
for x in range(10):
    soma += int(cpf[x]) * i
    i -= 1

if 11 - (soma % 11) > 9:
    digito_2 = 0
else:
    digito_2 = 11 - (soma % 11)
cpf += str(digito_2)

# Formatar CPF
cpf_formatado = f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

# Mostrar CPF na tela
tela = tkinter.Tk()
tela.withdraw()
print(f'CPF: {cpf}')
print(f'CPF formatado: {cpf_formatado}')
messagebox.showinfo('CPF', f'CPF: {cpf}\nCPF formatado: {cpf_formatado}')
