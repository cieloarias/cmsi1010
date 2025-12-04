import math
from dataclasses import dataclass
import pygame
import random
import sys

WIDTH, HEIGHT = 1024, 600
SKY_COLOR = (135, 240, 255)
GRASS_COLOR = (128, 255, 100)
GRASS_HEIGHT = 100
GRASS_TOP = HEIGHT - GRASS_HEIGHT
GRASS_RECTANGLE = (0, GRASS_TOP, WIDTH, GRASS_HEIGHT)
GROUND_LEVEL = HEIGHT - (GRASS_HEIGHT // 2)
TREE_SPACING = 173
MAX_PLANE_SPEED = 23
CRUISING_ALTITUDE = 50

# Runway visuals
RUNWAY_WIDTH = 500
RUNWAY_HEIGHT = 36
RUNWAY_LEFT = (WIDTH // 2) - RUNWAY_WIDTH // 2
RUNWAY_TOP = GRASS_TOP + (GRASS_HEIGHT - RUNWAY_HEIGHT) // 2
RUNWAY_COLOR = (40, 40, 40)
RUNWAY_STRIPE = (210, 210, 210)

# Plane color
PLANE_COLOR = (168, 201, 191)  # your chosen color

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plane Landing")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)

# Load background image
background_img = pygame.image.load("sunset.jpg").convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Clouds
clouds = [{"x": random.uniform(-200, WIDTH), "y": random.uniform(20, 160), "spd": random.uniform(0.2, 0.9)} for _ in range(7)]

@dataclass
class Plane:
    x: int
    y: int
    state: str = "flying"
    speed: int = MAX_PLANE_SPEED
    rotation: float = 0.0
    color: tuple = PLANE_COLOR

    def draw(self):
        base_coords = [
            (-16, 0), (-13, 2), (-15, 7), (-12, 7), (-8, 2), (-1, 2),
            (-6, 6), (-5, 6), (8, 2), (16, 2), (19, -2), (8, -2),
            (-5, -8), (-6, -8), (-1, -2), (-13, -2)
        ]
        rotated = base_coords if self.rotation == 0 else [
            (x * math.cos(self.rotation) - y * math.sin(self.rotation),
             x * math.sin(self.rotation) + y * math.cos(self.rotation))
            for x, y in base_coords
        ]
        coords = [(WIDTH//2 + 4*x, self.y - 4*y) for x, y in rotated]
        pygame.draw.polygon(screen, self.color, coords)

    def move(self):
        if self.state != "stopped":
            self.x += self.speed % TREE_SPACING
        if self.state == "flying":
            pass
        elif self.state == "descending":
            self.y += self.speed * 0.1
            if self.y >= GROUND_LEVEL:
                self.state = "crashed"
                self.color = (255, 0, 0)  # red when crashed
                self.speed = 0
                self.y = GROUND_LEVEL
        elif self.state == "landing":
            self.y += self.speed * 0.1
            if self.y >= GROUND_LEVEL:
                self.state = "touching"
                self.y = GROUND_LEVEL
        elif self.state == "touching":
            pass
        elif self.state == "down":
            pass
        elif self.state == "braking":
            self.speed -= 0.1
            if self.speed <= 0:
                self.speed = 0
                self.state = "stopped"
        elif self.state == "starting":
            self.y = GROUND_LEVEL
            self.speed += 0.1
            if self.speed >= MAX_PLANE_SPEED:
                self.speed = MAX_PLANE_SPEED
        elif self.state == "rising":
            self.y -= self.speed * 0.1
            if self.y <= CRUISING_ALTITUDE:
                self.y = CRUISING_ALTITUDE
                self.state = "flying"
                self.rotation = 0
                self.color = PLANE_COLOR  # reset color to your chosen color after rising


plane = Plane(0, y=CRUISING_ALTITUDE)


def draw_tree(x, y):
    trunk_w, trunk_h = 12, 26
    pygame.draw.rect(screen, (120, 60, 20), (x - trunk_w//2, y - trunk_h, trunk_w, trunk_h))
    pygame.draw.ellipse(screen, (34,139,34), (x-36, y-94, 72, 72))
    pygame.draw.ellipse(screen, (28,120,28), (x-44, y-70, 88, 56))
    pygame.draw.ellipse(screen, (40,160,60), (x-30, y-86, 60, 48))

def draw_runway():
    x = - (plane.x % RUNWAY_WIDTH) - RUNWAY_WIDTH
    while x < WIDTH:
        pygame.draw.rect(screen, RUNWAY_COLOR, (x, RUNWAY_TOP, RUNWAY_WIDTH, RUNWAY_HEIGHT))
        dash_w, dash_h = 28, 6
        start = x + 30
        while start < x + RUNWAY_WIDTH - 30:
            pygame.draw.rect(screen, RUNWAY_STRIPE,
                             (int(start), RUNWAY_TOP + RUNWAY_HEIGHT // 2 - dash_h // 2, dash_w, dash_h))
            start += dash_w * 2
        x += RUNWAY_WIDTH

def draw_clouds(dt):
    for c in clouds:
        c["x"] += c["spd"] * (dt * 60)
        if c["x"] > WIDTH + 100:
            c["x"] = -120
            c["y"] = random.uniform(20, 160)
            c["spd"] = random.uniform(0.2, 0.9)
        cx = int(c["x"])
        cy = int(c["y"])
        pygame.draw.ellipse(screen, (245,245,245), (cx-40, cy-12, 80, 28))
        pygame.draw.ellipse(screen, (250,250,250), (cx-28, cy-20, 56, 32))

score = 0
prev_state = plane.state

def draw_scene():
    dt = clock.get_time() / 1000.0 if clock.get_time() > 0 else 1/60
    
    # Draw background
    screen.blit(background_img, (0, 0))

    # Draw clouds
    draw_clouds(dt)

    # Grass
    pygame.draw.rect(screen, GRASS_COLOR, GRASS_RECTANGLE)

    # Runway
    draw_runway()

    # Trees
    x = (-plane.x) % TREE_SPACING
    while x < WIDTH + TREE_SPACING:
        tree_screen_x = int(x)
        runway_screen_left = RUNWAY_LEFT - plane.x
        runway_screen_right = runway_screen_left + RUNWAY_WIDTH
        if not (runway_screen_left - 40 < tree_screen_x < runway_screen_right + 40):
            draw_tree(tree_screen_x, GRASS_TOP)
        x += TREE_SPACING

    # Plane
    plane.draw()
    plane.move()

    # HUD
    score_surf = font.render(f"SCORE: {score}", True, (0,0,0))
    screen.blit(score_surf, (10, 10))
    instr = font.render("Controls: DOWN descend, UP raise/land, DOWN(touching) lower nose, RETURN brake", True, (0,0,0))
    screen.blit(instr, (10, 30))

    if plane.state in ["crashed", "stopped"]:
        instr_reset = font.render("Press R to play again", True, (200,0,0))
        screen.blit(instr_reset, (10, 50))

    pygame.display.flip()
    clock.tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and plane.state == "flying":
                plane.rotation = -0.2
                plane.state = "descending"
            elif event.key == pygame.K_UP and plane.state == "descending":
                plane.rotation = 0.2
                if plane.y < GROUND_LEVEL - 100:
                    plane.state = "rising"
                else:
                    plane.state = "landing"
            elif event.key == pygame.K_DOWN and plane.state == "touching":
                plane.rotation = 0
                plane.state = "down"
            elif event.key == pygame.K_RETURN and plane.state == "down":
                plane.state = "braking"
            elif event.key == pygame.K_RIGHT and plane.state == "stopped":
                plane.state = "starting"
            elif event.key == pygame.K_UP and plane.state == "starting" and plane.speed == MAX_PLANE_SPEED:
                plane.rotation = 0.1
                plane.state = "rising"
            elif event.key == pygame.K_r and plane.state in ["crashed", "stopped"]:
                plane.x = 0
                plane.y = CRUISING_ALTITUDE
                plane.state = "flying"
                plane.speed = MAX_PLANE_SPEED
                plane.rotation = 0
                plane.color = PLANE_COLOR  #resets to your chosen color

    prev_state = prev_state
    draw_scene()

    if prev_state != plane.state:
        if plane.state == "crashed":
            score -= 1
        elif plane.state == "down":
            score += 1
    prev_state = plane.state

