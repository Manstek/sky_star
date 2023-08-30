import pygame
from pygame.sprite import Sprite
from settings import Settings


class Star(Sprite):
    """Класс описывающий одну звезду."""

    def __init__(self, blue_sky):
        super().__init__()
        self.screen = blue_sky.screen
        self.settings = Settings()

        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def update(self):
        """Перемещает звезду вниз."""
        self.y += self.settings.star_speed
        self.rect.y = self.y

