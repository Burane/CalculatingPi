global rayon, n, h, w

def setup():
    size(800,800)
    
def draw():
    rayon = 300
    h = height/2
    w = width/2
    n = 60
    pi = PI
    background(51)
    for i in range(1,n+1):
        fill(255, 204, 0)
        triangle(h,w ,h+rayon*(-sin(2*pi/(n/2)*i)),h-rayon*(-cos(2*pi/(n/2)*i)) ,h+rayon*(sin(2*pi/(n/2)*i)),h-rayon*(cos(2*pi/(n/2)*i)))

    noLoop()
    
class Point:
    def __init__(self, x, y, h, w):
        self.x = x
        self.y = y
        fill(255, 204, 0)
        noStroke()
        ellipse(x,y,h,w)
