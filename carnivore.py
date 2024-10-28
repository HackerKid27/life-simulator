import pygame
from random import randint as rand
import math as m
import time as t

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

carnivores = pygame.sprite.Group()
male_carns = pygame.sprite.Group()
female_carns = pygame.sprite.Group()

class Carnivore(pygame.sprite.Sprite):
    def __init__(self, parent=None):
        super(Carnivore, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect()
        self.dir = rand(0, 179)
        self.life = t.time()
        if parent != None:
            self.speed = rand(parent.speed - 2, parent.speed + 2)
            self.life_span = rand(parent.life_span - 10, parent.life_span +10)
            self.rect.center = parent.rect.center
        else:
            self.speed = rand(2, 5)
            self.life_span = rand(10, 30)        
        
    def update(self):
        if rand(1, 20) == 20:
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
        if t.time()-self.life >= self.life_span:
            self.kill()

        
class MaleCarn(Carnivore):
    
    def __init__(self, parent=None):
        super(MaleCarn, self).__init__()
        self.surf.fill((255,0,0))
        
    def update(self):
        super(MaleCarn, self).update()


class FemaleCarn(Carnivore):
    
    def __init__(self, parent=None):
        super(FemaleCarn, self).__init__()
        self.surf.fill((255,255,0))
        self.pregnant = False
        
    def update(self):
        super(FemaleCarn, self).update()
        if pygame.sprite.spritecollideany(self, male_carns):
            if not self.pregnant:
                self.pregnant = True
                self.conception = t.time()
                self.due = rand(2, 7)
        if self.pregnant and t.time()-self.conception >= self.due:
            self.birth()        

    def birth(self):
        if rand(1, 7) < 4:
            new_carn = MaleCarn(parent=self)
            male_carns.add(new_carn)
            carnivores.add(new_carn)
        else:
            new_carn = FemaleCarn(parent=self)
            female_carns.add(new_carn)
            carnivores.add(new_carn)
        self.pregnant = False