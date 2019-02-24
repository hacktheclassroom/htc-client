"""htc_client.minigames.Phishing"""

import sys

import pygame
from pygame.locals import *

sys.path.append('..')
from common import Background

NAME = 'Phishing'
POINTS = 300
IMG = './minigames/img/phishing.png'

emails = [
    {
        'img': './minigames/img/email1.png',
        'malicious': False
    }

]


def main(player, surface, font, clock):

    title = font.render('Is this a Phishing email?', False, (0, 0, 0))
    good_button = pygame.Rect(1050, 100, 100, 100)
    bad_button = pygame.Rect(1050, 500, 100, 100)
    bg = Background('./minigames/img/phishing_background.jpg', [0, 0])
    email_pic = pygame.image.load('./minigames/img/email.png')

    email_number = 0

    while True:
        clock.tick(60)

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                # print(mouse_pos)
                if good_button.collidepoint(mouse_pos):
                    if emails[email_number]['malicious']:
                        return
                    else:
                        player.client.solve('Phishing', 'phishingftw')
                        return
                elif bad_button.collidepoint(mouse_pos):
                    if emails[email_number]['malicious']:
                        player.client.solve('Phishing', 'phishing ftw')
                    else:
                        return
                    #flag = 'testflag'
                    #player.client.solve(NAME, flag)
                    #return

        surface.fill([255, 255, 255])
        surface.blit(bg.image, bg.rect)
        surface.blit(title, (10, 10))

        email_img = pygame.image.load(emails[email_number]['img'])
        surface.blit(email_img, (50, 50))

        pygame.draw.rect(surface, [0, 212, 0], good_button)
        pygame.draw.rect(surface, [212, 0, 0], bad_button)

        pygame.display.flip()
