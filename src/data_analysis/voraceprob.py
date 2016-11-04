import random
random.seed()
def vorace(blocks):
    tower=[]
    hauteurs=[j[0] for j in blocks]
    hauteur=0
    tower.append(Block([0,1000,1000]))
    for j in blocks :
        if j.posersur(tower[-1]) :
            haut=j[0]
            test=float((haut-min(hauteurs))/(max(hauteurs)-min(hauteurs)))
            if (random.random()<test):
                tower.append(j)
                hauteur+=j[0]

    return hauteur,len(tower)
