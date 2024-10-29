#!/usr/bin/env python3
# the above is a shebang, for linux/unix OS's - it just tells the OS that
# this is an executable python file.

import pygame


# This is basically just the entire main file in a class to keep it clean,
# and also this would allow for parallel simulations via the threading
# module in the future.
class Simulation:

    def __init__(self):
        self.width = None
        self.height = None
        self.screen = None

        self.speed = 1
        self.is_running = False # this tells if the simulation loop is actually running
        self.is_paused = False # this can be used to pause/play the simulation without breaking the loop
        # I'm using a regular list for the animals, and just adding a tag to tell if they're
        # male/female (you could probably do the same to tell if they're a carnivore/herbivore)
        # You could use sprite Groups here, but the advantage of using a regular list is
        # that you can do "invisible" animals that aren't sprite based as well, while also
        # having more control over how they handle checks for collision, etc.
        # (also I've never rly used sprite groups before so this is probably mostly preference lol)
        self.carnivores = pygame.sprite.Group()

        self.herbivores = pygame.sprite.Group()


    # This just puts all the window setup code in a method, rather than __init__
    # since the main class isn't *just* dealing with window but also the main loop
    # and other things, it makes sense to put this separately. This would, for example,
    # allow multiple simulations to be run at the same time without each having their own
    # window.
    def display_init(self, width: int, height: int, gui=True):
        pygame.init() # Initializes pygame, connects pygame's abstractions to the host computer.
        pygame.display.init()
        self.width = width # Setting up the screen for the ecosystem window.
        self.height = height
        if gui:
            self.screen = pygame.display.set_mode((self.width, self.height))
            self.screen.fill((0,0,0)) # black


    # This starts the main loop running, with a speed modifier that can be
    # used to control how fast or slow the simulation should run.
    def run(self, speed=1):
        self.speed = speed
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():  # Checking if the program window has been terminated.
                if event.type == pygame.QUIT:  # If so, exits main loop.
                    self.is_running = False
                    self.is_paused = True

            if not self.is_paused: # If the simulation isn't paused, update the entities.
                self.update()

            # Clear the screen, and draw the simulation
            # The reason I split this into an update() and draw() methods is that you can
            # update the sim without drawing it, for running multiple simulations etc.
            # - and you can still have the simulation being rendered even when it's paused
            self.screen.fill((0, 0, 0))
            self.draw()


    # Updates the simulation, using the speed property to tell
    # how much to update them by.
    def update(self):
        self.carnivores.update(self.speed)
        self.herbivores.update(self.speed)


    # Draws the simulation to the screen. Adding a camera may be helpful in the future
    # As it would allow the simulation to go beyond the bounds of the window, and
    # then the view can be controlled independently.
    def draw(self):
        # I'm passing the screen instance to each carnivore object so you can reuse
        # the drawing code in the carnivore class. This will make it easier to made
        # updates to the drawing code, and to find it as the project grows.
        self.carnivores.draw(self.screen)
        self.herbivores.draw(self.screen)
        pygame.display.update() # Update and flip are basically the same
