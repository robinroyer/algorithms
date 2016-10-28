blocks=[]
for j in range(10):
    read=open("./data/b100_"+str(j),'r')
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

    class Block(list):
        def __init__(self,*args):
            list.__init__(self,*args)
            if self[0] < self[1] :
                tmp=self[0]
                self[0]=self[1]
                self[1]=tmp
        def posersur(self,block):
             return (block[1]>self[1] and self[0]<block[0])

    blocksbis=[]
    for j in extracted_data:
        blocksbis.append(Block(j))
        blocksbis.append(Block([j[0],j[2],j[1]]))
        blocksbis.append(Block([j[2],j[1],j[0]]))
    blocks.append(blocksbis)
