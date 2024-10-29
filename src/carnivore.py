import pygame, random, math, time
from django.utils.timezone import override

SCREEN_WIDTH = 1000 # Constants for the size of the ecosystem window.
SCREEN_HEIGHT = 750

carnivores = pygame.sprite.Group() # Groups to make it easier to reference sprites of the same class
male_carns = pygame.sprite.Group()
female_carns = pygame.sprite.Group()

class Carnivore(pygame.sprite.Sprite):
    
    def __init__(self, parent=None): # Runs when the herbivore class is initialized.
        super(Carnivore, self).__init__() # Sets up the visual aspects of the carnivore.
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect()
        self.dir = random.randint(0, 179)
        self.life = time.time()
        if parent != None: # Sets up traits inherited from the organism's parent.
            self.speed = random.randint(parent.speed - 2, parent.speed + 2) # Sets the speed the organism moves.
            self.life_span = random.randint(parent.life_span - 10, parent.life_span +10) # Sets the lifespan of the organism.
            # NOT YET WORKING: Moves child to parent's position on initialization.
            self.rect.center = parent.rect.center
        else: # Does the same using base metrics for the initial organisms.
            self.speed = random.randint(2, 5)
            self.life_span = random.randint(10, 30)        

    @override
    def update(self):
        if random.randint(1, 20) == 20: # Updates the position of the sprite.
            self.dir += random.randint(-45, 45)
        x_update = math.cos(self.dir*(math.pi/180))*self.speed
        y_update = math.sin(self.dir*(math.pi/180))*self.speed
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
        if time.time()-self.life >= self.life_span: # Checks if the organism has exceeded its lifespan.
            self.kill()

        
class MaleCarn(Carnivore):
    
    def __init__(self, parent=None): # Sets the color of the male carnivore.
        super(MaleCarn, self).__init__()
        self.surf.fill((255,0,0))
        
    def update(self):
        super(MaleCarn, self).update()


class FemaleCarn(Carnivore):
    
    def __init__(self, parent=None): # Sets the color of the male carnivore.
        super(FemaleCarn, self).__init__()
        self.surf.fill((255,255,0))
        self.pregnant = False
        
    def update(self):
        super(FemaleCarn, self).update()
        if pygame.sprite.spritecollideany(self, male_carns): # Check whether organism has become pregnant.
            if not self.pregnant:
                self.pregnant = True
                self.conception = time.time()
                self.due = random.randint(2, 7)
        if self.pregnant and time.time()-self.conception >= self.due: # Check whether baby is due.
            self.birth()        

    def birth(self): # Dynamic creation of new organisms.
        if random.randint(1, 7) < 4: # Female organisms are slightly(25%) more common.
            new_carn = MaleCarn(parent=self) # Create a new male carnivore
            male_carns.add(new_carn)
            carnivores.add(new_carn)
        else:
            new_carn = FemaleCarn(parent=self) # Create a new female carnivore
            female_carns.add(new_carn)
            carnivores.add(new_carn)
        self.pregnant = False
