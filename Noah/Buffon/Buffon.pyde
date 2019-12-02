hauteur = 500
largeur = 50
longueurAiguille = 50
nbAiguilles = 0
sacoupe = 0
vitesse = 500

def setup() :
    size(501, 500)
    i = 0
    j = 0
    for i in range(10):
        rectMode(CORNER)
        rect(largeur * i, 0, largeur, hauteur)

def draw() :
    for j in range(500):
        x1 = random(0, hauteur)
        y1 = random(0, hauteur)
        x2 = random(x1 - longueurAiguille, x1 + longueurAiguille)
        flag = random(-1, 1)
        if(flag > 0):
            y2 = y1 + sqrt(longueurAiguille**2 - (x2 - x1)**2)
        else :
            y2 = y1 - sqrt(longueurAiguille**2 - (x2 - x1)**2)
        sacoupetil(x1, x2)
        line(x1, y1, x2, y2)
        global nbAiguilles
        nbAiguilles += 1
    pi = (2 * float(longueurAiguille) * float(nbAiguilles)) / (float(sacoupe) * float(largeur))
    print pi

def sacoupetil(x1, x2):
    for k in range(0, 550, 50) :
        if((x1 <= k <= x2) or (x2 <= k <= x1)):
            global sacoupe
            sacoupe += 1
            return stroke(0, 255, 0)
        else:
            stroke(255, 0, 0)
