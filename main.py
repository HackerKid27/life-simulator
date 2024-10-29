import pygame
from random import randint as rand
import carnivore
import math as m
import time as t
from carnivore import MaleCarn, FemaleCarn, carnivores, male_carns, female_carns # See carnivore.py
from herbivore import MaleHerb, FemaleHerb, herbivores, male_herbs, female_herbs # See herbivore.py

pygame.init() # Initializes pygame, connects pygame's abstractions to the host computer.


SCREEN_WIDTH = 1000 # Setting up the screen for the ecosystem window.
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((0,0,0))


tiger = MaleCarn() # Initialize the starting organisms.
tigeress = FemaleCarn()
buck = MaleHerb()
doe = FemaleHerb()

male_carns.add(tiger) # Add the starting organisms to the right groups.
female_carns.add(tigeress)
male_herbs.add(buck)
female_herbs.add(doe)
carnivores.add(tiger, tigeress)
herbivores.add(buck, doe)


running = True # The main loop
while running:
    for event in pygame.event.get(): # Checking if the program window has been terminated.
        if event.type == pygame.QUIT: # If so, exits main loop.
            running = False
        

    screen.fill((0,0,0)) # Draws over past blits with a layer of black, the background color.

    for carn in carnivores: # Updates all carnivores and draws them in the window.
        carn.update() # See carnivore.Carnivore.update()
        screen.blit(carn.surf, carn.rect)

    for herb in herbivores: # Updates all herbivores and draws the in the window.
        herb.update() # See carnibore.Carnivore.update()
        screen.blit(herb.surf, herb.rect)

    pygame.display.flip() # Applies all the changes made to the window since the last flip.