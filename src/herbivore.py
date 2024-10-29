import pygame
from random import randint as rand
import math as m
import time as t

SCREEN_WIDTH = 1000 # Constants for the size of the ecosystem window.
SCREEN_HEIGHT = 750

herbivores = pygame.sprite.Group() # Groups to make it easier to reference sprites of the same class
male_herbs = pygame.sprite.Group()
female_herbs = pygame.sprite.Group()

class Herbivore(pygame.sprite.Sprite):
    
    def __init__(self, parent=None): # Runs when the herbivore class is initialized.
        super(Herbivore, self).__init__()
        self.surf = pygame.Surface((50, 50)) # Sets up the visual aspects of the herbivore.
        self.rect = self.surf.get_rect()
        self.dir = rand(0, 179)
        self.life = t.time()
        if parent != None: # Sets up traits inherited from the organism's parent.
            self.speed = rand(parent.speed - 2, parent.speed + 2) # Sets the speed the organism moves.
            self.life_span = rand(parent.life_span - 10, parent.life_span +10) # Sets the lifespan of the organism.
            # NOT YET WORKING: Moves child to parent's position on initialization.
            self.rect.centerx, self.rect.centery = parent.rect.centerx, parent.rect.centery
        else: # Does the same using base metrics for the initial organisms.
            self.speed = rand(2, 5)
            self.life_span = rand(10, 30)        
        
    def update(self):
        if rand(1, 20) == 20: # Updates the position of the sprite.
            self.dir += rand(-45, 45)
        x_update = m.cos(self.dir*(m.pi/180))*self.speed
        y_update = m.sin(self.dir*(m.pi/180))*self.speed
        self.rect.move_ip(x_update, y_update)
        if self.rect.left < 0:
            self.rect.left = 0
            self.dir += 180
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.dir += 180
        if self.rect.top <= 0:
            self.rect.top = 0
            self.dir += 180
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.dir += 180
        if t.time()-self.life >= self.life_span: # Checks if the organism has exceeded its lifespan.
            self.kill()

        
class MaleHerb(Herbivore):
    
    def __init__(self, parent=None):
        super(MaleHerb, self).__init__()
        self.surf.fill((0,0,255)) # Sets the color of the male herbivore.
        
    def update(self):
        super(MaleHerb, self).update()


class FemaleHerb(Herbivore):
    
    def __init__(self, parent=None):
        super(FemaleHerb, self).__init__()
        self.surf.fill((0,255,0)) # Sets the color of the female herbivore.
        self.pregnant = False
        
    def update(self):
        super(FemaleHerb, self).update()
        if pygame.sprite.spritecollideany(self, male_herbs): # Check whether organism has become pregnant.
            if not self.pregnant:
                self.pregnant = True
                self.conception = t.time()
                self.due = rand(2, 7)
        if self.pregnant and t.time()-self.conception >= self.due: # Check whether baby is due.
            self.birth()        

    def birth(self): # Dynamic creation of new organisms.
        if rand(1, 7) < 4: # Female organisms are slightly(25%) more common.
            new_herb = MaleHerb(parent=self) # Create a new male herbivore
            male_herbs.add(new_herb)
            herbivores.add(new_herb)
        else:
            new_herb = FemaleHerb(parent=self) # Create a new female herbivore
            female_herbs.add(new_herb)
            herbivores.add(new_herb)
        self.pregnant = False
