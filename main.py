from logger import  log_state
from constants import *
import pygame

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print(f"Screen width: {SCREEN_WIDTH}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log-state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        display.flip()
if __name__ == "__main__":
    main()

