#!/usr/bin/env python3
# I moved most of the code to its own class in simulation.py
# but this file is still the one that runs the program.
# It imports simulation.py and then creates an instance of a sim.

import simulation
from src.carnivore import MaleCarn, FemaleCarn
from src.herbivore import MaleHerb, FemaleHerb

# Make an instance of a simulation
sim = simulation.Simulation()
sim.display_init(800, 600) # width and height, leave gui blank if you want a window
sim.run() # leave speed blank for 1x speed

# HEADS UP: I only changed the main simulation code, I haven't done much
# any work on the actual entities yet. But I'm thinking it would make
# sense to have all the animals inherit from a parent class, (animal.py)
# and then just use tags since presumably you'll be checking

# THIS IS BROKEN RN BC THE CLASSES NEED TO BE EDITED FOR THE NEW SIM CODE
# ALSO I AM GOING TO TRY USING SPRITE GROUPS FOR THE ORGANISMS BECAUSE
# I THINK YOU CAN OVERRIDE THE UPDATE AND DRAW METHODS AS WELL AS HAVE
# ACCESS TO THE groupCollide METHOD FOR INTERACTIONS.

tiger = MaleCarn() # Initialize the starting organisms.
tigress = FemaleCarn()
buck = MaleHerb()
doe = FemaleHerb()

sim.carnivores.add(tiger)
sim.carnivores.add(tigress)
sim.herbivores.add(buck)
sim.herbivores.add(doe)