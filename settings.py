import pygame


class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 640 #720
        self.screen_height = 440 #500
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load('images/bg.png')

        # Ship settings.
        self.ship_speed = 1.5

        # Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1