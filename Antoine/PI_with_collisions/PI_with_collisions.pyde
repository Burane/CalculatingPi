


def setup():
   # frameRate(4)
    size(1500, 700)
    global block1, block2, masse1, masse2, digits, speed, cpt
    cpt = Compteur(0)
    print(cpt)
    nombres = 3
    masse1 = 100
    speed = 0
    masse2 = pow(100, nombres)
    block1 = Block(100,200,masse1,0)
    block2 = Block(300,200,masse2,-1)
 

def draw():
    print(cpt.val)
    background(51)
    
    if (block1.collide(block2)):
        v1 = block1.bounce(block2)
        v2 = block2.bounce(block1)
        block1.speed = v1
        block2.speed = v2
        cpt.incr()
        
    if (block1.hitWall()):
        block1.reverse()
        cpt.incr()
    
    block1.show()
    block2.show()
    block2.update()
    block1.update()
    
    textSize(68);
    fill(255, 204, 0)
    textAlign(CENTER);
    text(cpt.val, width/2, 500);


class Compteur:
    def __init__(self, val):
        self.val = val
        
    def incr(self) : 
        self.val += 1
    
class Block:
  def __init__(self, x, y, masse, speed):
    self.x = x
    self.y = y
    self.masse = masse
    self.speed = speed
    self.taille = log(masse)*10


  def hitWall(self):
    return (self.x - self.taille <= 0)


  def reverse(self) :
    self.speed = - self.speed


  def collide(self, other) :
    bordDroitO = other.x + other.taille
    bordGaucheO = other.x - other.taille
    bordDroitS = self.x + self.taille
    bordGaucheS = self.x - self.taille
    return not(bordGaucheS < bordGaucheO)


  def bounce(self, other) :
      sommeMasse = self.masse + other.masse
      sousMasse = self.masse - other.masse
      return ( ((sousMasse/sommeMasse)*self.speed) + (((2*other.masse)/sommeMasse)*other.speed) )

  def update(self) :
    self.x += self.speed;
  

  def show(self) :
    rectMode(CENTER)
    fill(255, 204, 0)
    noStroke()
    rect(self.x, self.y, self.taille, self.taille);
