"""HTC client menu"""

import sys

import pygame
from pygame.locals import *

from player import Player


class InputBox():
    """Pygame text input hack."""

    def __init__(self, x, y):
        self.font = pygame.font.Font(None, 36)
        self.inputBox = pygame.Rect(x, y, 300, 36)
        self.colorInactive = pygame.Color('gray')
        self.colorActive = pygame.Color('blue')
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
    button = pygame.Rect(600, 50, 50, 50)

    # text boxes
    username_text = font.render('Username', False, (0, 0, 0))
    server_code_text = font.render('Server Code', False, (0, 0, 0))
    error_text = font.render('Error! Server code invalid.', False, (0, 0, 0))

    # input boxes
    username = InputBox(250, 10)
    server_code = InputBox(250, 100)

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
                    results = player.client.validate()
                    if results['success']:
                        validated = True
                    else:
                        error = True

            username.handle_event(event)
            server_code.handle_event(event)

        surface.fill((233, 233, 233))
        username.draw(surface)
        server_code.draw(surface)
        pygame.draw.rect(surface, [212, 0, 0], button)

        surface.blit(username_text, (10, 10))
        surface.blit(server_code_text, (10, 100))

        # TODO: This doesn't work...?
        if display_error:
            surface.blit(error_text, (10, 150))

        pygame.display.flip()

        if validated:
            break

    return player
