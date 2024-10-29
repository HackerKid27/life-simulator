#!/usr/bin/env python3
# This is a main class to inherit all the other animal classes from,
# rather than using pygame.sprite.Sprite.

import enum

import pygame.sprite


class Animal(pygame.sprite.Sprite):

    def __init__(self):
        super(Animal, self).__init__() # Sets up the visual aspects of the carnivore.
