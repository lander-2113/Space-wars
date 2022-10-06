import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from alien import Alien
from button import Button
import game_functions as gf
"""
pygame.mixer.pre_init(44100, 16, 2, 4096)
>>> sound = pygame.mixer.Sound('audio/ship_collision.wav')
>>> sound.play()

"""

def run_game():

    # frequency, size, stereo, buffer.
    pygame.mixer.init(44100, 16, 2, 4096)
    # initialzie pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ai_settings.bg_image('bgimage.bmp')
    # make the play button.
    play_button = Button(ai_settings, screen, "Play")
    # cretae an instance to store game statistics and scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # make a ship, a group of bullets and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    alien = Alien(ai_settings, screen)

    # create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop for the the game.

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button,
                        ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)

if __name__ == '__main__':
    run_game()