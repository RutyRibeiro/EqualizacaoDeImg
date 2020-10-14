def apresenta():
    print('\033[33m{}\033[m\n'.format('-'*60))
    print('{:^60}'.format('PROGRAMA DE EQUALIZAÇÃO\n'))
    print('\033[33m{}\033[m'.format('-'*60))
    
def defineL(vet):
    L= len(vet)
    print(L)
    return L

def geraK(minElem, maxElem):
    K=[]
    for i in range(minElem, maxElem + 1):
        K.append(i)
    return K

def geraHk(K,linhaDeImg):
    Hk=[]
    for i in K:
        Hk.append(linhaDeImg.count(i))
    return Hk

def geraHaK (Hk):
    HaK=[]
    for index, elem in enumerate(Hk):
        if index == 0:
            HaK.append(elem)
        else:
            HaK.append(HaK[index - 1] + elem)
    return HaK

def geraPk (HaK, N):
    Pk=[]
    
    for i, elem in enumerate(HaK):
        Pk.append(elem / N)
    return Pk

def geraKlin(Pk, L):
    kLinha=[]
    for i,elem in enumerate(Pk): 
        kLinha.append(round(elem * (L - 1 ))) 
    return kLinha

def geraNovaLin (base,K,kLinha):
    linEqua=base
    controle=[]
    for i in range(len(linEqua)):
        controle.append(0)

    for index, elem in enumerate(K):
        for i,e in enumerate(linEqua):
            if e==elem and controle[i]==0:
                linEqua[i]=kLinha[index]
                controle[i]=1
    return linEqua



def novaLin(linhaDeImg, N):
    minElem = min(linhaDeImg)
    maxElem = max(linhaDeImg)
    base = linhaDeImg.copy()
    
    K= geraK(minElem,maxElem)
    L=defineL(K)
    Hk= geraHk(K, linhaDeImg)
    HaK= geraHaK(Hk)
    Pk= geraPk(HaK, N)
    kLinha= geraKlin(Pk, L)

    base = geraNovaLin (base,K,kLinha)

    return base