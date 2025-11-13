import pygame

import Constants
from Game import Game
from Renderer import Renderer

pygame.init()

screen = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))

renderer = Renderer(screen)
game = Game()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            game.handle_click(pos)

    renderer.draw(game.board)
pygame.quit()

