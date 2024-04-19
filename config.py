import pygame
import components

WIN_HEIGHT = 720
WIN_WIDTH = 550

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

ground = components.Ground(WIN_WIDTH)
pipes = []