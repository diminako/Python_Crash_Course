import pygame
import sys

class Blue_sky():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (50, 50, 230)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.screen.fill(self.bg_color)
                pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    bs = Blue_sky()
    bs.run_game()