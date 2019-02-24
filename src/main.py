"""htc-client"""

import sys

from htc_api import Client

# all the pygame imports
import pygame
import pygameMenu
from pygame.locals import *
from pygameMenu.locals import *

# globals
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
MENU_BACKGROUND_COLOR = (58, 58, 58)
WIDTH = 1280
HEIGHT = 720
WINDOW_SIZE = (WIDTH, HEIGHT)
MENU_FONT_SIZE = 36
MENU_ALPHA = 100

# init pygame
pygame.init()
pygame.font.init()

# TODO: Fix font
# myfont = pygame.font.Font('./font.ttf', 36)
myfont = pygame.font.Font(None, 36)
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Hack The Classroom')
clock = pygame.time.Clock()


class Player:
    def __init__(self, username, server_code):
        self.username = username
        self.server_code = server_code
        self.client = Client(self.username, self.server_code)
        self.points = 0


# button for input
button = pygame.Rect(600, 50, 50, 50)
# text
username_text = myfont.render('Username', False, (0, 0, 0))
server_code_text = myfont.render('Server Code', False, (0, 0, 0))
error_text = myfont.render('Error! Server code invalid.', False, (0, 0, 0))


class InputBox():
    def __init__(self, x, y):
        self.font = pygame.font.Font(None, 36)
        self.inputBox = pygame.Rect(x, y, 300, 36)
        self.colourInactive = pygame.Color('gray')
        self.colourActive = pygame.Color('blue')
        self.colour = self.colourInactive
        self.text = ''
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.inputBox.collidepoint(event.pos)
            self.colour = self.colourActive if self.active else self.colourInactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        txtSurface = self.font.render(self.text, True, self.colour)
        screen.blit(txtSurface, (self.inputBox.x+5, self.inputBox.y+5))
        pygame.draw.rect(screen, self.colour, self.inputBox, 2)


def main():

    validated, display_error = False, False
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

    # start game loop if validated
    # do things with pygame & player object
    print('things')


if __name__ == '__main__':
    main()
