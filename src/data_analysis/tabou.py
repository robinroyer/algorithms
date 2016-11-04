import random
import time
import sys
# safe sys.argv access
from get_argv import getArgv
from readblocks import Block
from triParSurface import triInsertionSurfaceDecroissant

def dynamiquetabou(blocks):
    tower=[]
    tabou=[]
    haut=0
    samehaut=0
    while samehaut<100 :
        towerbis=list(tower)
        block=blocks[random.randint(0,len(blocks)-1)]
        while (block in towerbis or block in tabou):
            block=blocks[random.randint(0,len(blocks)-1)]
        indexblock=0
        while (indexblock<len(tower) and block.posersur(tower[indexblock])):
            indexblock+=1
        towerbis.insert(indexblock,block)
        while (indexblock+1<len(towerbis) and not towerbis[indexblock+1].posersur(block)) :
            tabou.append([towerbis[indexblock+1],random.randint(8,11)])
            towerbis.remove(towerbis[indexblock+1])
        hautbis=sum([j[0] for j in towerbis])
        if hautbis>haut :
            haut=hautbis
            tower=towerbis
            samehaut=0
        else :
            samehaut+=1
        for j in tabou :
            if j[1]<1 :
                tabou.remove(j)
            else :
                j[1]-=1
    return haut,tower



# CONSTANTES
PRINT_TIME = "-t"
PRINT_BLOCK = "-p"

path = ""
option1 = ""
option2 = ""
options = ""

# le path de l'exemplaire considere
path = getArgv(1)
option1 = getArgv(2)
option2 = getArgv(3)

options = option1 + option2
# tableau de nombre a trier
extracted_data=[]
blocks = []

# lecture du fichier contenant l'exemplaire
read=open(path,'r')

j=0
for line in read :
    if j == 0 :
        taille = int(line)
    else :
        data = line.split( )
        for j in range(len(data)) :
            data[j]=int(data[j])
        extracted_data.append(data)
    j += 1

read.close()
blocksbis=[]
for j in extracted_data:
    blocksbis.append(Block(j))
    blocksbis.append(Block([j[1],j[2],j[0]]))
    blocksbis.append(Block([j[2],j[1],j[0]]))
blocks.append(blocksbis)

# Execution
t1= time.time()
hauteur, tower = dynamiquetabou(extracted_data)
t2= time.time()

# Affichage
if PRINT_BLOCK in options:
    print(" Les blocks dans l'ordre sont sont : \r\n")
    for num in tower:
        print(num)

# Affichage du temps d'execution
if PRINT_TIME in options:
    print(" Cet algorithme prend : ", t2 - t1, "secondes !\r\n")
