# En entrée, il faut les blocks ordonnées : appeler la fonction triInsertionSurface
def dynamique(blocksordonne):
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
    return towers,hauteurs
# on peut directement retourner la tour la plus grande et sa hauteur en retournant  :
#  max(hauteurs),towers[hauteurs.index(max(hauteurs))]
