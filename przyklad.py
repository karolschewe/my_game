import sys
import time
import pygame

wysokosc_okna = 500
kolor = (100,100,0)
miejsce = (100,100)
wielkosc = (50,50)

pygame.init()
screen = pygame.display.set_mode((wysokosc_okna,wysokosc_okna))

pygame.draw.rect(screen,kolor,(miejsce,wielkosc))


pygame.display.update()
time.sleep(2)


carImg = pygame.image.load('beniz.png')
screen.blit(carImg, (200,200))
pygame.display.update()
time.sleep(2)