import random
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mondrian")

# 🎨 Custom colors
CELESTE = (188, 213, 242)
VERDE_AGUA = (188, 233, 213)
AZUL = (130, 193, 248)

# Updated color palette
COLORS = [
    CELESTE, CELESTE, CELESTE,  # more likely to appear
    (0, 0, 0),       # black
    (233, 228, 248),     # light purple
    (171, 252, 238),     # azul claro
    (176, 119, 141),   # guinda
    VERDE_AGUA,
    AZUL
]

# Rectangle size padding
X_PADDING = int(WIDTH * 0.05)
Y_PADDING = int(HEIGHT * 0.05)
LINE_WIDTH = 5


def draw_and_split(rect, level):
    # Draw the rectangle filled and outlined
    pygame.draw.rect(screen, random.choice(COLORS), rect)
    pygame.draw.rect(screen, pygame.Color("black"), rect, LINE_WIDTH)

    # Stop splitting if conditions met
    if level == 0:
        return
    if rect.width < 2 * X_PADDING or rect.height < 2 * Y_PADDING:
        return

    # Split horizontally or vertically
    if rect.width > rect.height:
        x = random.randint(rect.left + X_PADDING, rect.right - X_PADDING)
        r1 = pygame.Rect(rect.left, rect.top, x - rect.left, rect.height)
        r2 = pygame.Rect(x, rect.top, rect.right - x, rect.height)
    else:
        y = random.randint(rect.top + Y_PADDING, rect.bottom - Y_PADDING)
        r1 = pygame.Rect(rect.left, rect.top, rect.width, y - rect.top)
        r2 = pygame.Rect(rect.left, y, rect.width, rect.bottom - y)

    # Recursive calls
    draw_and_split(r1, level - 1)
    draw_and_split(r2, level - 1)


def draw_scene():
    # Clear screen then draw outer rectangle to take up the whole display
    screen.fill(CELESTE)
    outer_rectangle = pygame.Rect(0, 0, WIDTH, HEIGHT)
    draw_and_split(outer_rectangle, 5)
    pygame.display.flip()


# Draw first scene
draw_scene()

# Main event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            raise SystemExit
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # A click "starts over" with a new scene!
            draw_scene()
