hauteur = 500
largeur = 50
nbAiguille = 500
longueurAiguille = 20

def setup() :
    size(500, 500)
    i = 0
    j = 0
    for i in range(10):
        rectMode(CORNER)
        rect(largeur * i, 0, largeur, hauteur)
    for j in range(nbAiguille):
        x1 = random(0, hauteur)
        y1 = random(0, hauteur)
        x2 = random(x1 - longueurAiguille, x1 + longueurAiguille)
        flag = random(-1, 1)
        if(flag > 0):
            y2 = y1 + sqrt(longueurAiguille**2 - (x2 - x1)**2)
        else :
            y2 = y1 - sqrt(longueurAiguille**2 - (x2 - x1)**2)
        line(x1, y1, x2, y2)

def draw() :
    print 'onche'
