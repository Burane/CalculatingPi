hauteur = 500
largeur = 50
nbAiguille = 500

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
        x2 = random(x1 - 10, x1 + 10)
        y2 = random(y1 - 10, y1 + 10)
        line(x1, y1, x2, y2)

def draw() :
    print 'onche'
