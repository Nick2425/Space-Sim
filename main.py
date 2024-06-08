import pygame, sys, cl
from pygame.locals import QUIT

pygame.init()
win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Hello World!')
pygame.font.init()

text = pygame.font.SysFont('Arial', 30)
def showTxt(texta):
    t = text.render(texta, text, True, (255,255,255)) 
    win.blit(t, (40,140))

def createObject(m, pos, radius, vi):
    obj = cl.Thing(m, pos, radius, vi)
check = False
acc = 0
while True:
   pygame.time.delay(int(1000*cl.precisionAccuracy))
   for event in pygame.event.get():
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
               createObject(10**(acc), pygame.math.Vector2(iP[0], iP[1]), 10, -Vec)
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   win.fill((255, 255, 255))
   if check == True:
    showTxt("Mass = 10^" + str(acc))
    acc += cl.precisionAccuracy*5
    acc = round(acc,1)
    v2 = pygame.math.Vector2(iP[0], iP[1])
    pygame.draw.line(win, (0,0,0), (v2.x, v2.y), pygame.mouse.get_pos(), 3)
   for x in cl.gameObjects:
       x.move()
       #print(x.pos, x.v)
   pygame.display.update()