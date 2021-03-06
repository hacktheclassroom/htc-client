"""htc_client.menu"""

import sys

import pygame
from pygame.locals import *

from player import Player
from common import Background


class InputBox():
    """Pygame text input hack."""

    def __init__(self, x, y, font=None):
        self.font = font if font else pygame.font.Font(None, 50)
        self.inputBox = pygame.Rect(x, y, 300, 50)
        self.colorInactive = pygame.Color('black')
        self.colorActive = pygame.Color('white')
        self.color = self.colorInactive
        self.text = ''
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.inputBox.collidepoint(event.pos)
            self.color = self.colorActive if self.active else self.colorInactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        txtSurface = self.font.render(self.text, True, self.color)
        screen.blit(txtSurface, (self.inputBox.x+5, self.inputBox.y+5))
        pygame.draw.rect(screen, self.color, self.inputBox, 2)


def run_menu(surface, font, clock):
    """HTC pygame menu, validates and returns a valid player object."""

    validated, display_error = False, False

    # button for running validation
    button = pygame.Rect(490, 440, 300, 50)

    # text boxes
    title_text = font.render('Hack The Classroom', False, (255, 255, 255))
    username_text = font.render('Username', False, (255, 255, 255))
    server_code_text = font.render('Server Code', False, (255, 255, 255))
    error_text = font.render('Server code invalid!', False, (255, 255, 255))
    start_text = font.render('Start', False, (255, 255, 255))

    # input boxes
    username = InputBox(490, 250, font=font)
    server_code = InputBox(490, 370, font=font)

    # img
    bg = Background('./minigames/img/chalkboard.jpg', [0,0])
    logo = pygame.image.load('./minigames/img/logo.png')
    logo.convert()

    while True:
        clock.tick(60)

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if button.collidepoint(mouse_pos):
                    # validate player on login button press
                    player = Player(username.text, server_code.text)
                    # will create a user if they don't exist
                    player.client.solve('foo', 'bar')
                    results = player.client.validate()
                    if results['success']:
                        return player
                    display_error = True

            username.handle_event(event)
            server_code.handle_event(event)

        surface.fill([255, 255, 255])
        surface.blit(bg.image, bg.rect)

        username.draw(surface)
        server_code.draw(surface)
        pygame.draw.rect(surface, [212, 0, 0], button)

        # 1280/2 - 150 = 490
        surface.blit(username_text, (490, 200))
        surface.blit(server_code_text, (490, 320))
        surface.blit(start_text, (600, 445))
        surface.blit(title_text, (490, 100))

        surface.blit(logo, (50, 50))

        if display_error:
            surface.blit(error_text, (500, 520))

        pygame.display.flip()
