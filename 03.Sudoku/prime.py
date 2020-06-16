diag_princip = 219456894



for num in range(diag_princip,-1,-1): ## testando numeros de 97 para baixo
    
    for i in range(2,num-1): ## testando se esse número é primo, começando com 2 até o próprio numero

        if num % i == 0:
            break
    else:
        if diag_princip % num == 0:
            print(num)
            exit()

