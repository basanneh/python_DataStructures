
def hanoi(n,source, aux, destination):

    if n == 1:
        print("Plate 1 from %s to %s"%(source,destination))
        return
    #moving n-1 plates off the largest one to be able to move that 
    hanoi(n-1,source,destination,aux)
    #moving the actual largest one
    print("Plate %s from %s to %s"%(n,source,destination))
    #placing n-1 plates on the top of the largest one
    hanoi(n-1,aux,source,destination)


hanoi(3,'A','B','C')
