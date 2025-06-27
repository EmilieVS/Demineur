# Générer la grille
# la fonction prend en paramètre ligne (l) et colone(c)

import random

def gridGenerator (l,c,b):

    maxbomb = l*c
    if b >= maxbomb :
        message = print("Wait there would be bombs everywhere")
        return message
   
    grid = [[ 0 for _ in range(c)] 
            for _ in range(l)]
    
    bomb = 0 
    
    
    while bomb < b :
        i = random.randint(0, l -1)
        j = random.randint(0, c -1)

        if grid[i][j] == 0:
            grid[i][j] = 1
            bomb+=1

    for row in grid:
       print(" ".join(str(cell) for cell in row))        
    

gridGenerator(5,5,25)
    


