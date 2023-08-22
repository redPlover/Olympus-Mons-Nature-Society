import pygame

#constants
WIDTH, HEIGHT = 100, 70


class PlayerHandler:
    def __init__(self, window_width, window_height):
        self.held_animals = []
        self.player = pygame.Rect(window_width//2, window_height//2, WIDTH, HEIGHT)
    
    def move_player():
        pass
    
    def interact():
        print("interaction")