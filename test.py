import time
import random
random.seed()
class Block(list):
    def __init__(self,*args):
        list.__init__(self,*args)
        if self[2] < self[1] :
            tmp=self[2]
            self[2]=self[1]
            self[1]=tmp
    def posersur(self,block):
         return (block[1]>self[1] and self[2]<block[2])

scope=[100,500,1000,5000,10000,50000,100000,500000]
blocks=[[] for j in scope]
def triSurfaceDecroissant(blocks):
    blocks=sorted(blocks,key=lambda bloc: bloc[0]*bloc[1],reverse=True)
    return blocks
def vorace(blockss):
    blocks= triSurfaceDecroissant(blockss)
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

    return hauteur
def dynamique(blocksordonnee):
    blocksordonne = triSurfaceDecroissant(blocksordonnee)
    towers=[]
    hauteurs=[]
    for block in blocksordonne :
        hauteurblock=[]
        indextower=[]
        peutEtrePoser= False

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

    return max(hauteurs)
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
    return haut


for s in scope :
    for j in range(10):
        read=open("./data/b"+str(s)+"_"+str(j),'r')
        extracted_data=[]
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
        blocks[scope.index(s)].append(blocksbis)
timer=[]
hauteur=[]
for sets in blocks[:3] :
	timerset=[]
	hauteurset=[]
	for jeu in sets :
		t1=time.time()
		hauteurset.append(dynamique(jeu))
		t2=time.time()
		timerset.append(t2-t1)
	timer.append(sum(timerset)/len(timerset))
	hauteur.append(sum(hauteurset)/len(hauteurset))
for x in range(len(timer)) :
	if x==0 :
		fichier = open("./collected_data/moyennedynamique.txt", "w")
		fichier.write(str(scope[x])+ ' '+str(timer[x]) +' '+str(hauteur[x]) )
		fichier.close()
	
	else :
		
		fichier = open("./collected_data/moyennedynamique.txt", "a")
		fichier.write("\n"+str(scope[x])+ ' '+str(timer[x]) +' '+str(hauteur[x]) )
		fichier.close()
