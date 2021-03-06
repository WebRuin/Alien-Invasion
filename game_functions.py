import sys
import pygame

def check_events(ship):
    """Respond to keypress and mouse events."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_f:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT or event.key == pygame.K_s:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_f:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT or event.key == pygame.K_s:
                ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)

    # render the ship
    ship.blitme()

    pygame.display.flip()
