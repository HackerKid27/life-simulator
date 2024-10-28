import pygame
from random import randint as rand
import carnivore
import math as m
import time as t
from carnivore import MaleCarn, FemaleCarn, carnivores, male_carns, female_carns
from herbivore import MaleHerb, FemaleHerb, herbivores, male_herbs, female_herbs


from pygame.locals import (
    QUIT,
    K_ESCAPE,
    KEYDOWN
)

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((0,0,0))


tiger = MaleCarn()
tigeress = FemaleCarn()
buck = MaleHerb()
doe = FemaleHerb()
male_carns.add(tiger)
female_carns.add(tigeress)
male_herbs.add(buck)
female_herbs.add(doe)
carnivores.add(tiger, tigeress)
herbivores.add(buck, doe)


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    screen.fill((0,0,0))

    for carn in carnivores:
        carn.update()
        screen.blit(carn.surf, carn.rect)

    for herb in herbivores:
        herb.update()
        screen.blit(herb.surf, herb.rect)

    pygame.display.flip()