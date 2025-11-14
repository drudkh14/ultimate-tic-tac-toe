import pygame

import Constants
from Game import Game
from Renderer import Renderer

pygame.init()

screen = pygame.display.set_mode((Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))
pygame.display.set_caption("Ultimate Tic Tac Toe")

renderer = Renderer(screen)
game = Game()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and game.game_started:
            pos = pygame.mouse.get_pos()
            game.handle_click(pos)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            game.reset()

        if not game.game_started:
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN or
                    (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1)):
                game.game_started = True

    renderer.draw(game)
pygame.quit()
