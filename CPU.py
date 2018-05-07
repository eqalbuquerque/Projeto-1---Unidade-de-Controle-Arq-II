# -*- coding: utf-8 -*-

from sys import argv


def carregar(arq="fatorial.txt",mem="memoria.txt"):

    programa, label, memoria = [],{},{}
    registrador = {"R1": 0, "R2": 0, "R3": 0, "R4": 0, "FLAGS": -1}

    with open(arq, 'r') as prog:
        x = 0
        for y in prog: 
            code = y.rstrip().split(" ")    #rstrip - retira do final da stringEx: \n \0  # recebe a string 
            if len(code) == 1 and code[0].endswith(":"):  # retornar o numero de elementos na lista
                label[code[0][:-1]] = x 
            programa.append(code)
            x += 1

    with open(mem,'r') as memo:
        pos = 1
        for x in memo: 
            memoria[("M" + str(pos))] = int(x)
            pos += 1


    dados = memoria.copy()
    dados.update(registrador)

    print(dados)

    PC, FIM = 0, len(programa)  #PC Controlador de Programa
    Clock = 0
    while PC < FIM:
        
        instrucao = programa[PC]
        print(instrucao)
        if instrucao[0] == 'MOV': 
            if instrucao[2].isdigit():
               dados[instrucao[1]] = int(instrucao[2])
            else:
                dados[instrucao[1]] = dados[instrucao[2]]
        elif instrucao[0] == 'INC':
            dados[instrucao[1]] += 1
        elif instrucao[0] == 'DEC':
            dados[instrucao[1]] -= 1
        
        elif instrucao[0] == 'ADD': 
            if instrucao[2].isdigit():
               dados[instrucao[1]] += int(instrucao[2])
            else:
                dados[instrucao[1]] += dados[instrucao[2]]
        
        elif instrucao[0] == 'SUB': 
            if instrucao[2].isdigit():
               dados[instrucao[1]] -= int(instrucao[2])
            else:
                dados[instrucao[1]] -= dados[instrucao[2]]

        elif instrucao[0] == 'MUL': 
            if instrucao[2].isdigit():
               dados[instrucao[1]] *= int(instrucao[2])
            else:
                dados[instrucao[1]] *= dados[instrucao[2]]

        elif instrucao[0] == 'DIV': 
            if instrucao[2].isdigit():
               dados[instrucao[1]] /= int(instrucao[2])
            else:
                dados[instrucao[1]] /= dados[instrucao[2]]

        elif instrucao[0] == 'EXP': 
            if instrucao[2].isdigit():
               dados[instrucao[1]] **= int(instrucao[2])
            else:
                dados[instrucao[1]] **= dados[instrucao[2]]

        # Pulo Incondicional
        elif instrucao[0] == 'JMP': 
            PC = label.get(instrucao[1])
        
        # Comparação
        elif instrucao[0] == 'CMP':
            flags = 0
            if instrucao[2].isdigit():
                flags = dados[instrucao[1]] - int(instrucao[2])
            else:
                flags = dados[instrucao[1]] - dados[instrucao[2]]
            if flags == 0: dados['FLAGS'] = 1 # IGUAL
            elif flags < 0: dados['FLAGS'] = 2 # menor
            elif flags > 0: dados['FLAGS'] = 3 # maior
            if instrucao[2].isdigit():
                if int(instrucao[2]) == 0:
                    if dados[instrucao[1]] == 0: dados['FLAGS'] = 0 # VALOR ZERO 
        

        # Pulo Condicional
        elif instrucao[0] == 'JZ': #PULO SE ZERO
            if dados['FLAGS'] == 0: PC = label.get(instrucao[1])
        elif instrucao[0] == 'JE': #PULO SE IGUAL
            if dados['FLAGS'] == 1: PC = label.get(instrucao[1])   
        elif instrucao[0] == 'JL': #PULO SE MENOR
            if dados['FLAGS'] == 2: PC = label.get(instrucao[1])
        elif instrucao[0] == 'JG': #PULO SE MAIOR
            if dados['FLAGS'] == 3: PC = label.get(instrucao[1])   
            
        print(dados)
        #Contagem Ciclos de Clock
        Clock += 1
        PC += 1
    print("Quantidade de Ciclos de Clock: " + str(Clock))

    with open(mem,'w') as salvar:
        iterador = 0
        for x in dados.values():
            if iterador >= len(memoria): break
            salvar.write(str(x) + "\n")
            iterador += 1


if len(argv) >= 2:
    carregar(argv[1])
else: carregar()
