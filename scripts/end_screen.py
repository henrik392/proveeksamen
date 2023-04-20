import pygame
from constants import *


def init(to_game_func, player):
    global to_game
    global player_won
    global text
    global text_rect
    global hint_text
    global hint_text_rect

    to_game = to_game_func

    text = pygame.font.Font(None, 36).render(
        f"{player_to_name[player]} won!", True, (255, 255, 255))

    hint_text = pygame.font.Font(None, 16).render(
        f"Press ESC to quit, R to restart", True, (180, 180, 180))

    text_rect = text.get_rect()
    hint_text_rect = hint_text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 12)
    hint_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 12)


def handle_events(events):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                to_game()


def draw(screen):
    screen.fill((0, 0, 0))

    screen.blit(text, text_rect)
    screen.blit(hint_text, hint_text_rect)

    pygame.display.update()


def update(dt, events, screen):
    handle_events(events)

    # Update game logic here

    draw(screen)
