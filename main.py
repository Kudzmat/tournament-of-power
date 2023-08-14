import pygame
import os

pygame.init()

# game window
STATS_PANEL = 250
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 680 + STATS_PANEL
CLOCK = pygame.time.Clock()
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tournament Of Power")


# load images

# background image
background_image = pygame.image.load("assets/stage/tournament-stage.png").convert_alpha()

# panel image
panel_image = pygame.image.load("assets/HUD/panel.png").convert_alpha()

character = pygame.image.load('assets/Characters/naruto/tile000.png').convert_alpha()
player_x = 110
player_y = 170


# function for drawing background
def draw_background():
    screen.blit(background_image, (0, 0))


def draw_panel():
    screen.blit(panel_image, (0, SCREEN_HEIGHT - STATS_PANEL))


# game loop
game_on = True
while game_on:
    CLOCK.tick(FPS)
    # draw stage
    draw_background()

    # draw panel
    draw_panel()

    screen.blit(character, (player_x, player_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

    pygame.display.update()

pygame.quit()
