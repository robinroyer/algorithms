import random
random.seed()
tower=[]
hauteurs=[j[2] for j in blocks[0]]
hauteur=0
tower.append(Block([1000,1000,0]))
for j in range(len(blocks[0])):
    if blocks[0][j].posersur(tower[-1]) :
        haut=blocks[0][j][2]
        test=float((haut-min(hauteurs))/(max(hauteurs)-min(hauteurs)))
        if (random.random()<test):
            tower.append(blocks[0][j])
            hauteur+=blocks[0][j][2]

print(hauteur,len(tower))
