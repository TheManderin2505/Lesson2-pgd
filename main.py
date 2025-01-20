import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen.fill("pink")

class Rect():
    def __init__(self,color,dimentions):
        self.rect_surface=screen
        self.rect_color=color
        self.rect_dimentions = dimentions

    def draw_rect(self):
        self.rec_draw = pygame.draw.rect(self.rect_surface,self.rect_color,self.rect_dimentions)

#boject'
greenRect = Rect(green,(50,2,100,120))
greenRect.draw_rect()
redRect = Rect(red,(60,3,110,130))
redRect.draw_rect()
whiteRect = Rect(white,(70,4,120,140))
whiteRect.draw_rect()
blackRect = Rect(black,(80,5,130,150))
blackRect.draw_rect()
blueRect = Rect(blue,(90,6,140,160))
blueRect.draw_rect()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.update()