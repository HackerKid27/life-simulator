import pygame, random, math, time
from django.utils.timezone import override


# Most of this can be moved into a basic animal class, but that's for later
class Carnivore(pygame.sprite.Sprite):
    
    def __init__(self, x: int, y: int, width: int, height: int, life_span: int, gender: str, parent=None):
        super(Carnivore, self).__init__() # Sets up the visual aspects of the carnivore.
        self.rect = pygame.Rect(x, y, width, height) # This is to avoid problems with instances
        self.image = pygame.Surface((self.rect.width, self.rect.height))
        self.dir = random.randint(0, 359) # Using degrees instead of radians
        self.speed = random.randint(1, 2)
        self.age = 0
        self.life_span = life_span
        self.gender = gender

        # Sets up traits inherited from the organism's parent.
        if parent is not None:
            self.rect.center = parent.rect.center


    def update(self, speed: int):
        print(self.gender + " carnivore, " + str(self.age) + " years old updated at " + str(speed) + "x speed")
        # Put all the update code here, multiplied by speed.
        # if random.randint(1, 20) == 20: # Updates the position of the sprite.
        #     self.dir += random.randint(-45, 45)
        # x_update = math.cos(self.dir*(math.pi/180))*self.speed
        # y_update = math.sin(self.dir*(math.pi/180))*self.speed
        # self.rect.move_ip(x_update, y_update)
        # if self.rect.left < 0:
        #     self.rect.left = 0
        #     self.dir += 180
        # if self.rect.right > SCREEN_WIDTH:
        #     self.rect.right = SCREEN_WIDTH
        #     self.dir += 180
        # if self.rect.top <= 0:
        #     self.rect.top = 0
        #     self.dir += 180
        # if self.rect.bottom >= SCREEN_HEIGHT:
        #     self.rect.bottom = SCREEN_HEIGHT
        #     self.dir += 180
        # if time.time()-self.life >= self.life_span: # Checks if the organism has exceeded its lifespan.
        #     self.kill()

    def draw(self, surface: pygame.surface.Surface):
        surface.blit(self.image, self.rect)

## ALL THE FOLLOWING CAN BE PUT INTO THE Carnivore CLASS
# Just use an if statement to differentiate between different update methods

# class FemaleCarn(Carnivore):
#
#     def __init__(self, parent=None): # Sets the color of the male carnivore.
#         super(FemaleCarn, self).__init__()
#         self.surf.fill((255,255,0))
#         self.pregnant = False
#
#     def update(self):
#         super(FemaleCarn, self).update()
#         if pygame.sprite.spritecollideany(self, male_carns): # Check whether organism has become pregnant.
#             if not self.pregnant:
#                 self.pregnant = True
#                 self.conception = time.time()
#                 self.due = random.randint(2, 7)
#         if self.pregnant and time.time()-self.conception >= self.due: # Check whether baby is due.
#             self.birth()
#
#     def birth(self): # Dynamic creation of new organisms.
#         if random.randint(1, 7) < 4: # Female organisms are slightly(25%) more common.
#             new_carn = MaleCarn(parent=self) # Create a new male carnivore
#             male_carns.add(new_carn)
#             carnivores.add(new_carn)
#         else:
#             new_carn = FemaleCarn(parent=self) # Create a new female carnivore
#             female_carns.add(new_carn)
#             carnivores.add(new_carn)
#         self.pregnant = False
