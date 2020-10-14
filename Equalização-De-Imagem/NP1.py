from equaliza import novaLin, apresenta
linhaDeImg=[]

# linhaDeImg =[0,0,4,6,8,8,4,7,8,9,9,4,3,2,3,8,2,2,1,0]
# N = 20

apresenta()

while True:
    try:
        N=int(input('Digite um valor para N \033[33m(Total de pixel na linha de imagem)\033[m: '))
        break
    except:
        print('\033[31mERRO!\033[m Digite um valor valor numérico válido!')
        

while True:
    if len(linhaDeImg) == N:
        break
    else:
        try:
            num = (int(input('Qual o valor do pixel? \033[32m(entre 0 e 255)\033[m')))
            linhaDeImg.append(num) 
        except:
            print('\033[31mERRO!\033[mDigite um valor numérico válido!')

linhaEqua = novaLin(linhaDeImg, N)

print(linhaEqua)
