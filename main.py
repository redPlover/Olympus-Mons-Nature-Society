import pygame
import os
import player_handler

# Constants
WIDTH, HEIGHT = 900, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 100, 70

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BACKGROUND = (0, 204, 0)

FPS = 60
clock = pygame.time.Clock()

vec = pygame.math.Vector2

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test Game")

class Player(pygame.Rect):
    def __init__(self):
        super().__init__(self, 0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT // 2 - self.height // 2

def draw_window(player):
    window.fill(BACKGROUND)
    pygame.draw.rect(window, GREEN, player)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if event.key == pygame.K_w:
                    player_handler.y += 1
                if event.key == pygame.K_a:
                    player_handler.x -= 1
                if event.key == pygame.K_s:
                    player_handler.y -= 1
                if event.key == pygame.K_d:
                    player_handler.x += 1
        
        player = Player()
        draw_window(player)

        pygame.display.flip()
        clock.tick(FPS)

if (__name__ == "__main__"):
    main()