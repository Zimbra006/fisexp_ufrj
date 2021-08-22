test = int(input('\nO que você quer testar?\nValores Estatísticos (1)\nCompatibilidade (2)\n'))

if test not in [1, 2]:
    test = int(input('Por favor, insira um valor válido para que eu faça a minha mágica\n'))

if test == 1:
    # Lista que vai armazenar os valores medidos
    x = eval(input('\nValores:'))

    def removeIndex():
        allClear = False
        while not allClear:
            for i in range(len(x)):
                if type(x[i]) == type(int()):
                    x.remove(x[i])
                    break
                if i == len(x) - 1:
                    allClear = True

    removeIndex()

    def media(values):
        return sum(values) / len(values)

    def desvPad(values):
        cValues = values[:]
        mean = media(values) 
        for x in range(len(cValues)):
            cValues[x] = (cValues[x] - mean) ** 2    
        return (sum(cValues) / (len(cValues) - 1)) ** (1 / 2)

    # # Comando para enontrar o Erro / Incerteza do Valor Médio
    def error(values):
        return desvPad(values) / ((len(values)) ** (1 / 2))

    # # Arredonda os valores para as casas decimais desejadas
    r = int(input("Quantas casas decimais? "))
    r_media = round(media(x), r)
    r_desvPad = round(desvPad(x), r)
    r_error = round(error(x), r)

    print("\nValores: ", x)
    print("Média Aritmética: ", r_media)
    print("Desvio Padrão: ", r_desvPad)
    print("Erro: ", r_error, "\n")
elif test == 2:
    
    # Pede pelos valores e suas respectivas discrepâncias
    x1 = float(input('\nValor 1: '))
    y1 = float(input('Discrepância 1: '))
    x2 = float(input('Valor 2: '))
    y2 = float(input('Discrepância 2: '))

    # Faz o cálculo da compatibilidade
    def compatibilidade(v1, d1, v2, d2):
        res = abs(v1 - v2) / ((d1**2 + d2**2)**(1/2))
        comp = res <= 3
        return [res, comp]
    
    comp = compatibilidade(x1, y1, x2, y2)

    # Responde a pergunta
    print(['Não são compatéveis', 'São compatíveis'][comp[1]] + ', pois o resultado é ' + 
            ['maior do que 3 (', 'menor ou igual a 3 ('][comp[1]] + str(comp[0]) + ')\n')
