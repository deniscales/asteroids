import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    run_the_game = True
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    new_player = Player(x, y, PLAYER_RADIUS)
    while run_the_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # Fill the screen with black
        new_player.draw(screen)
        pygame.display.flip()  # Update the display
        dt = clock.tick(60) / 1000  # Amount of seconds between each loop
        
     

if __name__ == "__main__":
    main()
