import numpy as np
import pygame
import sys

# initialize pygame
pygame.init()

# CONSTANTS
width = 600
height = width
line_width = 10
board_rows = 3
board_columns = 3
square_size = width // board_columns
color = (34, 40, 49)
line_color = (57, 62, 70)
circle_color = (0, 173, 181)
circle_radius = square_size // 3
circle_width = 20
cross_color = (238, 238, 238)
cross_width = 25
cross_space = square_size // 4
player = 1  # First player
is_over = False

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TIC TAC TOE GAME")
screen.fill(color)

board = np.zeros((board_rows, board_columns))


def draw_lines():
    # Horizontals
    pygame.draw.line(screen, line_color, (0, square_size), (width, square_size), line_width)
    pygame.draw.line(screen, line_color, (0, 2 * square_size), (width, 2 * square_size), line_width)

    # Verticals
    pygame.draw.line(screen, line_color, (square_size, 0), (square_size, height), line_width)
    pygame.draw.line(screen, line_color, (2 * square_size, 0), (2 * square_size, height), line_width)


def mark_square(row, column, player):
    board[row][column] = player


def available_square(row, columns):
    if board[row][columns] == 0:
        return True
    else:
        return False


def is_board_full():
    for rows in range(board_rows):
        for col in range(board_columns):
            if board[rows][col] == 0:
                return False
    return True


def draw_figures():
    for row in range(board_rows):
        for col in range(board_columns):
            if board[row][col] == 1:  # for player 1 circle
                pygame.draw.circle(screen, circle_color, (
                int(col * square_size + square_size // 2), int(row * square_size + square_size // 2)), circle_radius,
                                   circle_width)
            elif board[row][col] == 2:  # for player 2 cross
                pygame.draw.line(screen, cross_color,
                                 (col * square_size + cross_space, row * square_size + square_size - cross_space),
                                 (col * square_size + square_size - cross_space, row * square_size + cross_space),
                                 cross_width)
                pygame.draw.line(screen, cross_color,
                                 (col * square_size + cross_space, row * square_size + cross_space),
                                 (col * square_size + square_size - cross_space,
                                  row * square_size + square_size - cross_space), cross_width)


def check_win(player):
    # Vertical Win
    for col in range(board_columns):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            print("Player", player, "Won")
            return True
    # Horizontal Win
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            print("Player", player, "Won")
            return True
    # Left to Right Diagonal Win
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        print("Player", player, "Won")
        return True
    # Right to Left Diagonal Win
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print("Player", player, "Won")
        return True


def restart():
    screen.fill(color)
    draw_lines()
    for row in range(board_rows):
        for col in range(board_columns):
            board[row][col] = 0


# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not is_over:
            mouseX = event.pos[0]  # Mouse X Position
            mouseY = event.pos[1]  # Mouse Y Position
            clicked_row = int(mouseY // square_size)  # Clamping for rows
            clicked_column = int(mouseX // square_size)  # Clamping for columns
            if available_square(clicked_row, clicked_column):
                mark_square(clicked_row, clicked_column, player)
                if check_win(player):
                    is_over = True
                player = player % 2 + 1
                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                is_over = False
                player = 1
    pygame.display.update()
    draw_lines()
