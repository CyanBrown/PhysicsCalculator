#Python Physics Calculator
#####Author: Cyan Brown
***
####Starting Notes
***
* gravitational constant is 9.8
* air resistance considered negligible
* There are some random errors that I am working out
***
####Kinematics
***
#####Params:
######*All params are integer or float
* A (acceleration)
* T (total time)
* V0 (velocity initial)
* V (velocity final)
* X0 (position initial)
* X (position final)
***
####Projectile
***
#####Params:
* Initial Vector
    * from_vector (list) (required)
        * index 0 (str) options
            * 'x': calculate x vector as normal kinematic from above
            * 'y': calculate y vector as normal kinematic from above
            * 'projectile': calculate y and x vector using kinematics from above and calculate graph values
        * index 1 (int or float): magnitude of composite vector
        * index 2 (int or float): radians or degrees from horizontal axis
    * measure (str) (assumes deg)
        * 'deg': type of unit for from_vector[2] is degree
        * 'rad': type of unit for from_vector[2] is radian
        
***
####Shared Params
***
#####Params:
* round_to (int) (asummed 3) = set how many decimal places to round to

###Examples
***
[More Examples](https://github.com/CyanBrown/PhysicsCalculator/blob/master/example.py)
