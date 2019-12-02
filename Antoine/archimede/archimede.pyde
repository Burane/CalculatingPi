gobal rayon, n,h,w

def setup():
    size(800,800)
    rayon = 300
    h = height/2
    w = width/2
    
def draw():
    background(51)
    triangle(h,w,)
    
    
    
class Point:
    def __init__(self, x, y, h, w):
        self.x = x
        self.y = y
        fill(255, 204, 0)
        noStroke()
        ellipse(x,y,h,w)
