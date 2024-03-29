import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Initialize the game, and create game resources.'''
        pygame.init()
        # calling the settings from settings.py to be able to be used in self.settings
        self.settings = Settings()
        # Screen size parameters set by the settings pages.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # The title displayed
        pygame.display.set_caption("Alien Invasion")
        # Initiate the ship class when Alien Invasion initiates.
        self.ship = Ship(self)

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        # Respond to keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # Redraw the screen during each pass through the loop.  Pulled info from settings.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()