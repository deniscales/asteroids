import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

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
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)  # Assuming these are defined elsewhere
    Asteroid.containers = (asteroids, updatable, drawable)  # Assuming these are defined elsewhere
    AsteroidField.containers = (updatable)  # Assuming these are defined elsewhere

    asteroid_field = AsteroidField()
    new_player = Player(x, y, PLAYER_RADIUS)


    while run_the_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))  # Fill the screen with black
        for each in updatable:
            each.update(dt)
        for each in asteroids:
            if each.collsion(new_player):
                print("Game Over!")
                run_the_game = False
        for each_drawable in drawable:
                each_drawable.draw(screen)
      #  new_player.update(dt)

      #  new_player.draw(screen)
        pygame.display.flip()  # Update the display
        dt = clock.tick(60) / 1000  # Amount of seconds between each loop
        
     

if __name__ == "__main__":
    main()
