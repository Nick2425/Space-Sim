import pygame, math, os

bO = True
G = 6.67 * 10**-11
gameObjects = []

precisionAccuracy = 0.05


def dist(main, other):
  dx = main.pos.x - other.pos.x
  dy = main.pos.y - other.pos.x
  return math.sqrt(dx**2 + dy**2)

scale = 3.8*10**8/250

def getNet(obj):
  net = pygame.math.Vector2(0,0)
  for x in gameObjects:
    if obj != x:
      d = dist(obj, x)*scale
      n = G * x.mass / d**2
      net += n * vec(obj, x)

  return net
 # (3.8 * 10^8)m/250px
class Thing():
  def __init__(self, mass, pos, radius, v):
    gameObjects.append(self)
    self.mass = mass
    self.pos = pos
    self.radius = radius
    
    self.vi = v
    self.v = pygame.math.Vector2(0,0) + self.vi
    self.a = pygame.math.Vector2(0,0)
  def showVector(self):
    if bO == True:
      pygame.draw.line(pygame.display.get_surface(), (0,0,0), self.pos, self.pos + self.v, width=3)      

  def showField(self):
    for i in range(1, 18):
      if bO == True:
        pygame.draw.circle(pygame.display.get_surface(), (128, 128, 128, 20), self.pos, self.radius + self.radius*1.5**i, 1)

  def move(self):
    pygame.draw.circle(pygame.display.get_surface(), (255,0,0), (self.pos.x, self.pos.y), self.radius)
    self.showField()
    self.showVector()
    self.collide()
    self.a = getNet(self)
    self.v += self.a
    self.pos += self.v*0.05



  def collide(self):
    for x in gameObjects:
      if x != self:
        if x.pos.x > self.pos.x - self.radius and x.pos.x < self.pos.x + self.radius:
          if x.pos.y < self.pos.y + self.radius and x.pos.y > self.pos.y - self.radius:
            self.mass += x.mass 
            self.radius *= x.mass/self.mass + 1

            self.v = (self.mass * self.v + x.mass * x.v)/(x.mass + self.mass)

            gameObjects.remove(x)
            del x

def vec(obj1, obj2):
  
  dx = obj2.pos.x - obj1.pos.x
  dy = obj2.pos.y - obj1.pos.y
  Vec = pygame.math.Vector2(dx, dy)
  if Vec.length() > 1:
    Vec.normalize()
  return Vec