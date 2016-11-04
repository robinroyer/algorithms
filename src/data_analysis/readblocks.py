class Block(list):
    def __init__(self,*args):
        list.__init__(self,*args)
        if self[2] < self[1] :
            tmp=self[2]
            self[2]=self[1]
            self[1]=tmp
    def posersur(self,block):
         return (block[1]>self[1] and self[2]<block[2])
