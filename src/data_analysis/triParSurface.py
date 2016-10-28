def triInsertionSurfaceDecroissant(blocks):
    aires = [j[0]*j[1] for j in blocks]
    for i in range(len(aires)):
        x = aires[i]
        y = Block(blocks[i])
        j = i
        while (j>0 and aires[j-1]<x) :
            aires[j] = aires[j-1]
            blocks[j] = blocks[j-1]
            j = j-1
        aires[j] = x
        blocks[j] = y
    return blocks
