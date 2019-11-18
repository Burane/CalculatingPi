def setup():
    size(1500, 700)
    global block1, block2, masse1, masse2, digit
    digit = 4
    masse1 = 100
    masse2 = pow(100, digits - 1)
    block1 = Block(10,200,masse1,10)
    block2 = Block(700,200,masse2,10)

def draw():
    background(51)
    block1.show()
    block1.update()
    
    block2.show()
    block2.update()



class Block:
  def __init__(self, x, y, masse, vitesse):
    self.x = x
    self.y = y
    self.masse = masse
    self.vitesse = vitesse


  def hitWall(self):
    return (self.x <= 0)


  def reverse(self) :
    self.vitesse = - self.vitesse


  def collide(self, other) :
    return (self.x < other.x or self.x > other.x)


  def bounce(self, other) :
      sommeMasse = self.masse + other.masse
      sousMasse = self.masse - other.masse
      self.vitesse = ( ((sousMasse/sommeMasse)*self.vitesse) + (((2*other.masse)/sommeMasse)*other.vitesse) )

  def update(self) :
    self.x += self.vitesse;
  

  def show(self) :
    fill(255, 204, 0)
    noStroke()
    rect(self.x, self.y, self.masse*2, self.masse*2);
