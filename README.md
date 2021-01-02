# Python Physics Calculator

# Purpose

[Explain what this does in general terms] 

# Usage 

##### Author: Cyan Brown
***
#### Starting Notes
***
* gravitational acceleration is 9.8
* air resistance considered negligible
* There are some random errors that I am working out
***
#### Physics Class
***
##### Params:
###### *All params are integer or float
* A (acceleration)
* T (total time)
* V0 (velocity initial)
* V (velocity final)
* X0 (position initial)
* X (position final)
* vector (list) (required for projectile)
    * Index 0 - magnitude of vector
    * Index 1 - degrees or radians from x axis
* round_to (int) (asummed 3) = set how many decimal places to round to
* measure (str) (degree mode assumed) - deg for degree, rad for radian
***
#### Vector Types:
***
* magnitude angle vector (referred to as 'mag_ang')
    * represented as list with 2 floats [magnitude, degrees (or radians) from initial position]
* x part, y part vector (referred to as 'xy')
    * represented as list with 2 floats [x component, y component]
 

***
#### physicsObject class
***
   
##### Init Params:
* mass = mass of object in kilograms
* force_vector = the applied force on the object (uses one of the above vector types)
* static_friction_coefficient = the coefficient of static friction
* kinetic_friction_coefficient = the coefficient of kinetic friction
* measure = 'deg' for degree or 'rad' for radian, used for magnitude angle vector type
* starting_velocity = if the object is already moving, this is the velocity
* vector_type (default to 'mag_ang') = the type of vector given in parameter 'force_vector'

#### Methods
* ##### data_at_position:
    * **Params**
        * position = the position you want physics kinematics from
* ##### data_at_time:
    * **Params**
        * time = the time you want physics kinematics from
* ##### graph_fbd:
    * **Params**
        * save (bool) (default false) = if you want to save the graph
                        
***
#### staticPhysics functions
***
##### Common Params:
* measure (default 'deg') = defines measure of angle in magnitude angle vector
* ROUND_TO = entire file variable that set number of digits to round to
##### to_composite_vector:
* vector = mag_ang vector
##### to_magnitude_angle_vector:
* vector = xy vector
##### combine_vector_magnitude_angle:
* *argsv = mag_ang vectors
##### combine_vector_composition:
* *argsv = xy vectors
##### generate_random_vector:
* range1 (list [float, float]) = range that you want the first number of the vector to be in
* range2 (list [float, float]) = range that you want the second number of the vector



***
### Examples
***
Y to Time             |  X to Time           
:--------------------:|:--------------------:|
 ![](examples/ty_example.png)|  ![](examples/tx_example.png)

Y to X                |Y and X to Time
:--------------------:|:--------------------:|
![](examples/xy_example.png)|![](examples/all_example.png)

Free Body Diagram     |
:--------------------:|
![](examples/15,%20%5B100,%2035%5D.jpg)|

[More Examples](https://github.com/CyanBrown/PhysicsCalculator/tree/master/examples)

### Known Issues
* You cannot add custom kinematic values for projectiles, it only works with vectors alone

# Contributing

[In this section we will beging to define how anyone 
who will contribute is to make such a contribution]
