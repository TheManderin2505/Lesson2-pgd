import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Drawing a Circle")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    screen.fill("light blue")

    pygame.draw.circle(screen,(255,0,0),(400,300),50)
    pygame.display.update()

