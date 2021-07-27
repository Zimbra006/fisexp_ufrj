# Importa funções relacionadas a estatística
from statistics import *
from math import sqrt

# Lista que vai armazenar os valores medidos
x = list()

# Comando para adicionar valores na lista
def add():
    values = eval("[" + input("\nLista de Valores: ") + "]")
    for value in values:
        x.append(value)

# Comando para enontrar o Erro / Incerteza do Valor Médio
def error(values):
    return stdev(values) / sqrt(len(values))

# Pede ao usuário para que informe os valores a serem usados
add()

# Arredonda os valores para as casas decimais desejadas
r = int(input("Quantas casas decimais? "))
r_mean = round(mean(x), r)
r_stdev = round(stdev(x), r)
r_error = round(error(x), r)

print("\nValores: ", x)
print("Média Aritmética: ", r_mean)
print("Desvio Padrão: ", r_stdev)
print("Erro: ", r_error, "\n")