import pygame, sys, cl
from pygame.locals import QUIT
pygame.init()


info = pygame.display.Info()
win = pygame.display.set_mode((info.current_w, info.current_h))
pygame.display.set_caption('Hello World!')
pygame.font.init()

text = pygame.font.SysFont('Arial', 30)
square_w = info.current_w - info.current_h
square_w /= 2

obj1 = cl.Thing(10**26, pygame.math.Vector2(square_w, 0.5*info.current_h), 10, pygame.math.Vector2(0,-10))
obj2 = cl.Thing(10**26, pygame.math.Vector2((info.current_w-square_w, 0.5*info.current_h)), 10, pygame.math.Vector2(0,10))

def showTxt(a):
    i = 0
    for x in a:
        i += 1
        t = text.render(x, text, True, (255,255,255)) 
        win.blit(t, (40,140+40*i))

def createObject(m, pos, radius, vi):
    obj = cl.Thing(m, pos, radius, vi)
check = False
acc = 0

e1 = pygame.event.custom_type()
d = []
d.append("Planet = 10^24")
d.append("Moon = 10^22")
n = 0
while True:
   
   pygame.time.delay(int(1000*cl.precisionAccuracy))
   for event in pygame.event.get():
       keys = pygame.key.get_pressed()
       if keys[pygame.K_r]:
           cl.gameObjects.clear()
       if event.type == e1:
           n = 0
       if event.type == pygame.MOUSEBUTTONDOWN:
            if check != True:
               acc = 0
               check = True
               iP = pygame.mouse.get_pos()
        
       if event.type == pygame.MOUSEBUTTONUP:
           if check == True:
               check = False
               eP = pygame.mouse.get_pos()
               Vec = pygame.math.Vector2(eP[0]-iP[0], eP[1]-iP[1])
               createObject(10**(acc), pygame.math.Vector2(iP[0], iP[1]), 10, 2*-Vec)
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   win.fill((255, 255, 255))
   if check != True:
       showTxt(d)
   if check == True:
    eP = pygame.mouse.get_pos()
    Vec = pygame.math.Vector2(eP[0]-iP[0], eP[1]-iP[1])
    a = []
    a.append("Mass = 10^" + str(acc))
    a.append("Speed = " + str((2*-Vec).magnitude()))
    showTxt(a)
    acc += cl.precisionAccuracy*3
    acc = round(acc,1)
    v2 = pygame.math.Vector2(iP[0], iP[1])
    pygame.draw.line(win, (0,0,0), (v2.x, v2.y), pygame.mouse.get_pos(), 3)
   for x in cl.gameObjects:
       keys = pygame.key.get_pressed()
       x.move()
       if keys[pygame.K_h]:
         if n != 1:
             n += 1
             cl.bO = not(cl.bO)
             pygame.time.set_timer(e1, 2500, 1)
       #print(x.pos, x.v)
   pygame.display.update()