from readblocks import Block

def triSurfaceDecroissant(blocks):
    blocks=sorted(blocks,key=lambda bloc: bloc[0]*bloc[1],reverse=True)
    return blocks
