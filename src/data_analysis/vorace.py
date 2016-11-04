import random
import time
import sys
# safe sys.argv access
from get_argv import getArgv
from readblocks import Block
from triParSurface import triInsertionSurfaceDecroissant


def vorace(blocks):
    blocks = triInsertionSurfaceDecroissant(blocks)
    random.seed()
    tower=[]
    hauteurs=[j[0] for j in blocks]
    hauteur=0
    tower.append(Block([1000,1000,0]))
    for j in blocks :
        if j.posersur(tower[-1]) :
            haut=j[0]
            test=float((haut-min(hauteurs))/(max(hauteurs)-min(hauteurs)))
            if (random.random()<test):
                tower.append(j)
                hauteur+=j[0]

    return hauteur,tower


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

# Execution du MergeSort
t1= time.time()
hauteur, tower = vorace(extracted_data)
t2= time.time()

# Affichage du tri
if PRINT_BLOCK in options:
    print(" Les blocks dans l'ordre sont sont : \r\n")
    for num in tower:
        print(num)

# Affichage du temps d'execution
if PRINT_TIME in options:
    print(" Cet algorithme prend : ", t2 - t1, "secondes !\r\n")
