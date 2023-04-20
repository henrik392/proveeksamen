if __name__ == "__main__":
    raise Exception("This file is not to be run by the user")

import pygame
from constants import *
from functools import partial
from time import sleep

# Make margin by adding two invisible columns on each side
radius = SCREEN_WIDTH // (((COLUMNS+2) * (1 + MARGIN_RATIO))*2)


def draw_circle(screen, row, column, color):
    x = (column+1) * (radius * 2 * (1+MARGIN_RATIO)) + \
        radius * (1 + MARGIN_RATIO)
    y = (ROWS - row) * (radius * 2 * (1+MARGIN_RATIO))
    pygame.draw.circle(screen, color, (x, y), radius)


def valid_pos(column, row):
    return column >= 0 and column < COLUMNS and row >= 0 and row < len(board[column])


def check_win(column, row):
    player = board[column][row]
    # Check horizontal
    right = column
    left = column
    while (valid_pos(right, row) and board[right][row] == player):
        right += 1

    while (valid_pos(left, row) and board[left][row] == player):
        left -= 1

    if right - left - 1 >= CONNECT_TO_WIN:
        return True

    # Check vertical, only need to check down
    bottom = row
    while (valid_pos(column, bottom) and board[column][bottom] == player):
        bottom -= 1

    if row - bottom >= CONNECT_TO_WIN:
        return True

    # Check diagonal up right
    top_pos = (column, row)
    bottom_pos = (column, row)
    while (valid_pos(*top_pos) and board[top_pos[0]][top_pos[1]] == player):
        top_pos = (top_pos[0] + 1, top_pos[1] + 1)

    while (valid_pos(*bottom_pos) and board[bottom_pos[0]][bottom_pos[1]] == player):
        bottom_pos = (bottom_pos[0] - 1, bottom_pos[1] - 1)

    if top_pos[1] - bottom_pos[1] - 1 >= CONNECT_TO_WIN:
        return True

    # Check diagonal up left
    top_pos = (column, row)
    bottom_pos = (column, row)
    while (valid_pos(*top_pos) and board[top_pos[0]][top_pos[1]] == player):
        top_pos = (top_pos[0] - 1, top_pos[1] + 1)

    while (valid_pos(*bottom_pos) and board[bottom_pos[0]][bottom_pos[1]] == player):
        bottom_pos = (bottom_pos[0] + 1, bottom_pos[1] - 1)

    return top_pos[1] - bottom_pos[1] - 1 >= CONNECT_TO_WIN


def board_is_full():
    for column in board:
        if len(column) < ROWS:
            return False

    return True


# GAME STATE:
# Contains draw functions to be called on draw()
draw_queue = []

# Columns first, then rows
board = []

player = 1


def init(to_end_screen_func):
    global to_end_screen
    global draw_queue
    global board

    to_end_screen = to_end_screen_func

    draw_queue = [lambda screen: pygame.draw.rect(
        screen, GAME_COLOR, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))]

    board = []
    for column in range(COLUMNS):
        board.append([])
        for row in range(ROWS):
            draw_function = partial(
                draw_circle, row=row, column=column, color=player_to_color[0])
            draw_queue.append(draw_function)


def handle_events(events):
    global player

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            x, y = pygame.mouse.get_pos()

            column = int((x // (SCREEN_WIDTH / (COLUMNS+2))))

            if column == 0 or column == COLUMNS+1:
                break

            column -= 1

            # Check if column is full
            if len(board[column]) == ROWS:
                print("Column is full!!")
                break

            board[column].append(player)

            draw_function = partial(
                draw_circle, row=len(board[column])-1, column=column, color=player_to_color[player])
            draw_queue.append(draw_function)

            if check_win(column, len(board[column])-1):
                to_end_screen(player)

            if board_is_full():
                to_end_screen(0)

            player = 1 if player == 2 else 2


def draw(screen):
    for render_function in draw_queue:
        render_function(screen=screen)

    draw_queue.clear()

    pygame.display.update()


def update(dt, events, screen):
    handle_events(events)

    # Update game logic here

    draw(screen)
