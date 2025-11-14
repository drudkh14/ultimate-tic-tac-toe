from sndhdr import tests

import pygame.display
import Constants
import Game
from Constants import WINDOW_HEIGHT


class Renderer:

    def __init__(self, screen):
        self.screen = screen
        pygame.init()

    def draw(self, game):
        self.screen.fill(Constants.COLORS["BACKGROUND"])

        if game.board.global_winner:
            if game.board.global_winner == 'D':
                end_text = ("Freude hat gewonnen!!!\n"
                            "Wenn Sie nochmal\nspielen wollen\ndruecken Sie bitte auf 'R'!\n")
            else:
                end_text = (f"{game.board.global_winner} hat gewonnen!!!\n"
                            f"Wenn Sie nochmal\nspielen wollen\ndruecken Sie bitte auf 'R'\n")
            font = pygame.font.Font(None, 60)
            self.draw_text(end_text, font)

        if not game.game_started:
            font = pygame.font.Font(None, 60)
            self.draw_text(Constants.START_TEXT, font)
        elif not game.board.global_winner:
            for big_row in range(3):
                for big_col in range(3):
                    self.draw_mini_board(game.board, big_row, big_col)

            self.draw_big_grid()
        pygame.display.flip()

    def draw_text(self, text, font):
        lines = text.split("\n")
        temp_surf = font.render(lines[0], True, Constants.COLORS["TEXT"])
        line_height = temp_surf.get_height()
        total_height = len(lines) * line_height - (len(lines) - 1) * Constants.GAP
        y = (Constants.WINDOW_HEIGHT // 2) - (total_height // 2)
        for line in lines:
            text_surf = font.render(line, True, Constants.COLORS["TEXT"])
            text_rect = text_surf.get_rect()
            text_rect.centerx = Constants.WINDOW_WIDTH // 2
            text_rect.top = y
            self.screen.blit(text_surf, text_rect)
            y += text_rect.height + Constants.GAP


    def draw_mini_board(self, big_board, big_row, big_col):
        mini_board = big_board.boards[big_row][big_col]

        start_x = Constants.GAP + big_col * Constants.BIG_CELL_SIZE
        start_y = Constants.GAP + big_row * Constants.BIG_CELL_SIZE

        if big_board.active_board == (big_row, big_col):
            pygame.draw.rect(self.screen, Constants.COLORS["ACTIVE"],
                             (start_x - Constants.GAP, start_y - Constants.GAP,
                              Constants.BIG_CELL_SIZE, Constants.BIG_CELL_SIZE))

        if mini_board.winner and mini_board.winner != 'D':
            if mini_board.winner == 'X':
                self.draw_x(start_x, start_y, 0, 0, Constants.BIG_CELL_SIZE - 2 * Constants.GAP, 0)
            elif mini_board.winner == 'O':
                self.draw_o(start_x, start_y, 1, 1, Constants.BIG_CELL_SIZE // 2 - Constants.GAP, 0)
        else:
            for row in range(Constants.SMALL_CELL_NUMBER):
                for col in range(Constants.SMALL_CELL_NUMBER):
                    cell = mini_board.cells[row][col]
                    if cell.value == 'X':
                        self.draw_x(start_x, start_y, row, col, Constants.CELL_SIZE - 2 * Constants.INNER_GAP,
                                    Constants.INNER_GAP)
                    elif cell.value == 'O':
                        self.draw_o(start_x, start_y, row, col, Constants.CELL_SIZE // 2, Constants.INNER_GAP)

        self.draw_cell(start_x, start_y)

    def draw_big_grid(self):
        self.draw_vertical_lines()
        self.draw_horizontal_lines()

    def draw_vertical_lines(self):
        start_pos = Constants.BIG_CELL_SIZE
        for i in range(Constants.BIG_CELL_NUMBER - 1):
            pygame.draw.line(self.screen, Constants.COLORS["BIG_LINE"],
                             (start_pos, 0), (start_pos, Constants.WINDOW_HEIGHT), Constants.THICK)
            start_pos += Constants.BIG_CELL_SIZE

    def draw_horizontal_lines(self):
        start_pos = Constants.BIG_CELL_SIZE
        for i in range(Constants.BIG_CELL_NUMBER - 1):
            pygame.draw.line(self.screen, Constants.COLORS["BIG_LINE"],
                             (0, start_pos), (Constants.WINDOW_WIDTH, start_pos), Constants.THICK)
            start_pos += Constants.BIG_CELL_SIZE

    def draw_cell(self, start_x, start_y):
        self.draw_small_vertical_lines(start_x, start_y)
        self.draw_small_horizontal_lines(start_x, start_y)

    def draw_small_vertical_lines(self, start_x, start_y):
        pos_X = start_x + Constants.CELL_SIZE
        end_Y = (start_y + Constants.CELL_SIZE * Constants.SMALL_CELL_NUMBER +
                 (Constants.THIN * (Constants.SMALL_CELL_NUMBER - 1)))
        for i in range(Constants.SMALL_CELL_NUMBER - 1):
            pygame.draw.line(self.screen, Constants.COLORS["SMALL_LINE"],
                             (pos_X, start_y), (pos_X, end_Y), Constants.THIN)
            pos_X += Constants.CELL_SIZE

    def draw_small_horizontal_lines(self, start_x, start_y):
        pos_Y = start_y + Constants.CELL_SIZE
        end_X = start_x + Constants.CELL_SIZE * Constants.SMALL_CELL_NUMBER + (
                Constants.THIN * (Constants.SMALL_CELL_NUMBER - 1))
        for i in range(Constants.SMALL_CELL_NUMBER - 1):
            pygame.draw.line(self.screen, Constants.COLORS["SMALL_LINE"],
                             (start_x, pos_Y), (end_X, pos_Y), Constants.THIN)
            pos_Y += Constants.CELL_SIZE

    def draw_x(self, bx, by, row, col, size, gap):
        x1_start = bx + col * Constants.CELL_SIZE + gap
        y1_start = by + row * Constants.CELL_SIZE + gap
        x1_end = x1_start + size
        y1_end = y1_start + size
        x2_start = x1_start
        y2_start = y1_end
        x2_end = x1_end
        y2_end = y1_start
        pygame.draw.line(self.screen, Constants.COLORS["X"],
                         (x1_start, y1_start), (x1_end, y1_end), Constants.X_THICKNESS)
        pygame.draw.line(self.screen, Constants.COLORS["X"],
                         (x2_start, y2_start), (x2_end, y2_end), Constants.X_THICKNESS)

    def draw_o(self, bx, by, row, col, radius, gap):
        x = bx + col * Constants.CELL_SIZE + Constants.CELL_SIZE // 2
        y = by + row * Constants.CELL_SIZE + Constants.CELL_SIZE // 2

        pygame.draw.circle(self.screen, Constants.COLORS["O"], (x, y), radius - gap, Constants.O_THICKNESS)
