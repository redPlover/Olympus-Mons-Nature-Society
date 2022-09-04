import pygame
import os

# Constants
WIDTH, HEIGHT = 900, 600

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
                    player.y += 1
                if event.key == pygame.K_a:
                    player.x -= 1
                if event.key == pygame.K_s:
                    player.y -= 1
                if event.key == pygame.K_d:
                    player.x += 1

        window.fill(BACKGROUND)
        pygame.display.flip()
        clock.tick(FPS)

if (__name__ == "__main__"):
    main()