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
