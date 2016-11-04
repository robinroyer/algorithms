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
