import sys

import pygame

from settings import Settings

Class AlienInvasion:
    """Overall Class to manage game assets and behavior."""
    
    def_init_(self):
    """Initialize the game, and create game resources."""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        
        #Set the background Color
        self.bg_color = (230, 230, 230)
        
    def run_game(self):
    """Start the main loop for the game"""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get()
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            # Redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)
                    
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            
if_name_=='_main_':
    #Make a gmae instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
    