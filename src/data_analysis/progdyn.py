import random
import time
import sys
# safe sys.argv access
from get_argv import getArgv
from readblocks import Block
from triParSurface import triSurfaceDecroissant

# En entrée, il faut les blocks ordonnées : appeler la fonction triInsertionSurface
def dynamique(blocksordonne):
    blocksordonne = triSurfaceDecroissant(blocksordonne)
    towers=[]
    hauteurs=[]
    for block in blocksordonne :
        hauteurblock=[]
        indextower=[]
        peutEtrePoser= False
        # on check chacune des tours créés pour savoir si on peut poser notre block
        # et on rajoute une tour avec la meilleure base et le block en haut
        # si aucune tour ne correspond, on crée une nouvelle tour avec ce block
        for tower in towers :
            if block.posersur(tower[-1]) :
                peutEtrePoser=True
                hauteurblock.append(block[0]+hauteurs[towers.index(tower)])
                indextower.append(towers.index(tower))
        if peutEtrePoser :
            best=hauteurblock.index(max(hauteurblock))
            towers.append(towers[indextower[best]]+[block])
            hauteurs.append(hauteurblock[best])
        else :
            towers.append([block])
            hauteurs.append(block[0])
        # Au final, on obtient un nombre de tours égale au nombre de blocks de départ et il nous suffit de chercher la tour
        # la plus haute
    return max(hauteurs),towers[hauteurs.index(max(hauteurs))]
# on peut directement retourner la tour la plus grande et sa hauteur en retournant  :
#  max(hauteurs),towers[hauteurs.index(max(hauteurs))]




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


t1= time.time()
hauteur, tower = dynamique(blocksbis)
t2= time.time()

# Affichage
if PRINT_BLOCK in options:
    print(" Les blocks dans l'ordre sont sont : \r\n")
    for num in tower:
        print(num)

# Affichage du temps d'execution
if PRINT_TIME in options:
    print(" Cet algorithme prend : ", t2 - t1, "secondes !\r\n")
