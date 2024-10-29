#!/usr/bin/env python3
# I moved most of the code to its own class in simulation.py
# but this file is still the one that runs the program.
# It imports simulation.py and then creates an instance of a sim.

import simulation
import carnivore

# Make an instance of a simulation
sim = simulation.Simulation()
sim.display_init(800, 600) # width and height, leave gui blank if you want a window

# HEADS UP: I only changed the main simulation code, I haven't done much
# any work on the actual entities yet. But I'm thinking it would make
# sense to have all the animals inherit from a parent class, (animal.py)
# and then just use tags since presumably you'll be checking

# THIS IS BROKEN RN BC THE CLASSES NEED TO BE EDITED FOR THE NEW SIM CODE
# ALSO I AM GOING TO TRY USING SPRITE GROUPS FOR THE ORGANISMS BECAUSE
# I THINK YOU CAN OVERRIDE THE UPDATE AND DRAW METHODS AS WELL AS HAVE
# ACCESS TO THE groupCollide METHOD FOR INTERACTIONS.

# Initialize the starting organisms.
tiger = carnivore.Carnivore(300, 350, 60, 60, 20, "male")
tiger.image.fill((255, 0, 0)) # red for male
tigress = carnivore.Carnivore(100, 500, 50, 50, 22, "female")
tigress.image.fill((0, 0, 255)) # blue for female
# buck = MaleHerb()
# doe = FemaleHerb()

sim.carnivores.add(tiger)
sim.carnivores.add(tigress)
# sim.carnivores.add(tigress)
# sim.herbivores.add(buck)
# sim.herbivores.add(doe)


sim.run() # leave speed blank for 1x speed