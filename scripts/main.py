import pygame
from constants import *
import end_screen
import game

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Connect 4")

pygame.mixer.music.load("sounds/namgang.mp3")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
dt = 0


def to_end_screen(winner):
    global current_screen
    current_screen = end_screen
    end_screen.init(to_game, winner)


def to_game():
    global current_screen
    current_screen = game
    game.init(to_end_screen)


# to_game()
to_end_screen(0)
running = True
while running:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    current_screen.update(dt, events, screen)

    dt = clock.tick(FPS) / 1000

pygame.mixer.stop()
pygame.quit()
