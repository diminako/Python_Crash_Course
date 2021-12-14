import sys
import pygame

from settings import Settings

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

        # Set the background color
        # self.bg_color(230, 230, 230)

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.  Pulled info from settings.
            self.screen.fill(self.settings.bg_color)
            
            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()