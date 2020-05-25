import pygame
from math import pi

pygame.init()
pygame.display.set_caption('Thermal Cam')


screen = pygame.display.set_mode((500, 300))
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)
GREEN = pygame.Color(0, 255, 0)
YELLOW = pygame.Color(255, 255, 0)
TURQUOISE = pygame.Color(0, 255, 255)
PURPLE = pygame.Color(255, 0, 255)
BLACK = pygame.Color(0, 0, 0)

screen.fill(WHITE)

color = pygame.Color(0, 0, 0)

pygame.draw.rect(screen, color, (100,50,30,40), 1) #Drawing the rectangle

# Use surface
lcd = pygame.Surface((32, 32))
lcd.fill(YELLOW)

rect = pygame.Rect((50, 100), (32, 32))

screen.blit(lcd, rect)

pygame.display.update() 