r = 200
inside = 0
outside = 0
vitesse = 500000

def setup() :
    size(r*2+1, r*2+1)
    rectMode(CORNER)
    rect(0, 0, r*2, r*2)
    ellipseMode(CORNER)
    ellipse(0, 0, r*2, r*2)

def draw() :
    strokeWeight(1)
    translate(width/2, height/2)
    pie = 0
    for _ in range (vitesse) :
        x = random(-r, r)
        y = random(-r, r)
        d = x*x + y*y
        if(d < r*r):
            global inside
            inside = inside + 1
            stroke(0, 255, 0)
        else :
            global outside
            outside = outside + 1
            stroke(255, 0, 0)
        point(x, y)
    pie = float(4) * (float(inside) / float(outside + inside))
    print pie
