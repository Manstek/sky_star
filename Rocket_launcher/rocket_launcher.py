import pygame
import sys


from settings import Settings
from star import Star


class Sky:
    """Класс для управления ресурсами и поведениями игры."""
    def __init__(self):
        pygame.init()
        self.settings = Settings() 

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Star sky")

        self.stars = pygame.sprite.Group()
        self._create_fleet()


    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self._stars_update()
            self._update_screen()
    

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)


    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_q:
            sys.exit()
    

    def _create_star(self, star_number, row_number=1):
        """Создание звезды и размещение её в ряду."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.y = 2 * star.rect.height * row_number
        star.rect.y = star.y
        self.stars.add(star)


    def _create_fleet(self):
        """Создание звёздного неба."""
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        available_space_y = self.settings.screen_height - (2 * star_height)
        number_rows = available_space_y // (2 * star_height)

        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)
        
    
    def _new_row(self):
        """Создание нового ряда звёзд."""
        self.settings.tmp = self.settings.tmp + self.settings.star_speed
        star = Star(self)
        star_width, star_height = star.rect.size
        if self.settings.tmp >= star_height * 2:
            star = Star(self)
            available_space_x = self.settings.screen_width - (2 * star_width)
            number_stars_x = available_space_x // (2 * star_width)
            for star_number in range(number_stars_x):
                self._create_star(star_number)
            self.settings.tmp = 0


    def _stars_update(self):
        """Обновляет позиции звёзд в небе и создаёт новые ряды."""
        self.stars.update()
        self._new_row()


    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    blue_sky = Sky()
    blue_sky.run_game()

