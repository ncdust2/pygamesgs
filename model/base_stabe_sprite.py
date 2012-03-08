#!/usr/bin/env python
#coding:utf-8

import pygame
from pygame.sprite import Sprite

class BaseStableSprite(Sprite):
    def __init__(self, img, pos):
        Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = pos
