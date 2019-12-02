global cpt, diametre
def setup():
    size(700, 700)
    diametre = 1
    cpt = 0
    
def draw():
    rayon = 320
    cpt = 0
    margeErreur = 0.007
    background(51)
    fill(255, 204, 0)
    noStroke()
    center = Point(height/2,width/2,10,10)
    cercle(rayon,cpt,margeErreur,center,0)
    print(cpt)
    noLoop()
    
def cercle(rayon,cpt,margeErreur,center,bool):
    tabX = []
    tabY = []
    stroke(255, 204, 0)
    noFill()
    beginShape()
    noFill()
    for pixelX in range(height*2):
        for pixelY in range(width*2):
            distance = dist(center.x,center.y,pixelX,pixelY) 
            if ( distance >= rayon and distance <= rayon + margeErreur):
                cpt = cpt+1
                if (cpt %2 == bool):
                    tabX.append(pixelX)
                    tabY.append(pixelY)
                    vertex(pixelX, pixelY);
                    Point(pixelX,pixelY,10,10)
    endShape()
    sum = 0;
    for i in range(len(tabX)-1):
        sum = sum + (dist(tabX[i],tabY[i],tabX[i+1],tabY[i+1]))
    print("sum = ")
    print(sum/(rayon))
    
class Point:
    def __init__(self, x, y, h, w):
        self.x = x
        self.y = y
        fill(255, 204, 0)
        noStroke()
        ellipse(x,y,h,w)
