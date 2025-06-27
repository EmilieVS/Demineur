# Générer la grille
# la fonction prend en paramètre ligne (l) et colone(c)
# la jonction entre ligne est colone est une case. 
 # grid = [[0,0,0] on veut ce résultat là. C'est une liste de liste liste imbriquée.
    #      [0,0,0]
    #      [0,0,0]
    #     ]


def gridGenerator (l,c):
   
    grid = [[ 0 for _ in range(l)] 
            for _ in range(c)]
    print(grid)

gridGenerator(8,9)
    


