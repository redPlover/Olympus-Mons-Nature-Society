import pygame

# Constants
WIDTH, HEIGHT = 100, 70


class animal(pygame.sprite.Sprite):
    def __init__(self, type, color):
        super().__init__()
        self.type = type
        self.color = color
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)