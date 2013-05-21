ParticleSimulator
=================

Particle simulator for Kaback's AP C class.  The simulator is written in python for easy readability and portability.  This project depends on the VPython libraries (open source). 


In order to use, make Particles() in the simstart.py file. Run with "python simstart.py".  Global environmental constants are in the Particle.py file.

An old implementation of collision detection lies in the oldCollisions.py.  It does not work in its current state and may or may not be more efficient. (Implements modified A* Search algorithm which (theoretically) increases the efficiency for large quantities of simultaneous collisions. (Tree.py is a part of this old implementation).

The Vector.py file has all the vector operations.  "Flatten3" is an orthoganol projection onto a vector, but optimized for 3 dimensions. 

Note that all quantities are in SI base units (ie, length in meters, temperature in Celcius, etc.)

Have fun with it!


