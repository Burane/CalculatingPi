r = 200

def setup() :
    size(201, 201)
    rectMode(CENTER)
    rect(100, 100, 200, 200)
    ellipse(100, 100, r, r)

def draw() :
    strokeWeight(2)
    x = random(-r, r)
    y = random(-r, r)
    d = sqrt(x*x + y*y)
    if(d < r):
        stroke(0, 255, 0)
    else :
        stroke(255, 0, 0)
    point(x, y)
