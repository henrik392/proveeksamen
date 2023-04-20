FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_WIDTH = 700
GAME_HEIGHT = 500
MARGIN_RATIO = 0.2  # 20% of the circle radius

ROWS = 6
COLUMNS = 7
CONNECT_TO_WIN = 4

# BG_COLOR = (108, 164, 239)
BG_COLOR = (255, 255, 255)
GAME_COLOR = (21, 104, 205)
PLAYER_ONE_COLOR = (255, 0, 0)
PLAYER_TWO_COLOR = (0, 255, 0)

player_to_color = {
    0: (255, 255, 255),
    1: PLAYER_ONE_COLOR,
    2: PLAYER_TWO_COLOR
}

player_to_name = {
    0: "Nobody",
    1: "Player 1 (red)",
    2: "Player 2 (green)"
}
