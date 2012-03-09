#!/usr/bin/env python
#coding:utf-8

import pygame
from pygame.locals import QUIT,MOUSEBUTTONDOWN
from config import *
import sys 

class BaseFrame:
    def __init__(self, width, height, title, background, mouse):
        pygame.init()
        
        self.screen = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption(title)
        self.background = background
        self.mouse = mouse
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)
        self.loadImg()

    def loadImg(self):

        self.background = pygame.image.load(self.background).convert_alpha()
        self.mouse_cursor = pygame.image.load(self.mouse).convert_alpha()

    def run(self):
        self.loop()

    def loop(self):
        while True:

            self.handleEvents()
            self.draw()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_down(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_up(event)
            elif event.type == pygame.KEYDOWN:
                self.key_down(event)
            elif event.type == pygame.KEYUP:
                self.key_up(event)

    def draw(self):

        self.clock.tick(FPS)
        self.screen.blit(self.background,(0,0))
        x,y = pygame.mouse.get_pos()
        x -= self.mouse_cursor.get_width()/2
        y -= self.mouse_cursor.get_height()/2
        self.screen.blit(self.mouse_cursor, (x, y))

        pygame.display.update()

    def mouse_down(self,event):
        pass

    def mouse_up(self,event):
        pass

    def key_down(self,event):
        pass

    def key_up(self,event):
        pass
