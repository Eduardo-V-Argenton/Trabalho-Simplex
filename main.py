
def entrada():
    num_var = 1
    while(num_var != 0 ):
        num_var = int(input('Digite a quantidade de Variavies: '))
        if(num_var < 0):
            print('Valor inválido')
            continue
        elif(num_var == 0):
            break

        fo_type = int(input('Digite 1 para Max e 0 Min: '))
        if(fo_type != 0 and fo_type != 1):
            print('Valor inválido')
            continue

        fo = []
        i = 0
        while i < num_var:
            value_fo = float(input(f'Insira o valor {i}: '))
            fo.append(value_fo)
            i = i + 1

        num_rest = int(input('Digite a quantidade de restrições: '))
        rest = []
        i = 0
        while i < num_rest:
            print(f'Insira os valores da restrição {i}')
            h = 0
            line = []
            while h < num_var:
                value_rest = float(input(f'Digite o valor de x{h}: '))
                h = h + 1
                line.append(value_rest)
            value_rest = float(input(f'Digite o resultado de x{h}: '))
            line.append(value_rest)
            rest.append(line)
            i = i + 1
        
        i = 0
        no_n = []
        while i < num_var:
            no_n_value = int(input(f'A variavel x{i} é: (>0 --> 0), (>= 0 --> 1), (0< --> 2), (0<= --> 3): '))
            if(no_n_value != 0 and no_n_value != 1 and no_n_value != 2 and no_n_value != 3):
                print('Valor inválido')
                continue
            no_n.append(no_n_value)
            i = i + 1

        print('----------------------------------------')
        
        if(fo_type == 0):
            print('FO min(z) = ', end='')
        else:
            print('FO max(z) = ', end='')
        
        i = 0
        for i in range(0, num_var):
            print(f'+ {fo[i]}x{i}', end=' ')
        
        print('\n')

        for i in range(0, num_var):
            print(f'x{i}', end=', ')
        
        print('\n')

        for i in range(0, num_rest):
            for h in range(0, num_var):
                print(f'+ {rest[i][h]}x{i}', end=' ')
            print(f'= {rest[i][h + 1]}')
        
        print('\n')
        for i in range(0, num_var):
            if(no_n[i] == 0):
                print(f'x{i} > 0')
            elif(no_n[i] == 1):
                print(f'x{i} >= 0')
            elif(no_n[i] == 2):
                print(f'x{i} < 0')
            else:
                print(f'x{i} <= 0')
        
        print('\n\n')

entrada()


