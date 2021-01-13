# Python Physics Calculator
##### Author: Cyan Brown
***
#### Starting Notes
***
* gravitational acceleration is 9.81
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
* vector (initial vector if projectile)

***
#### Vector Class:
***

##### Init Params
* vector_type (composite or mag_ang)
* data1 (x component, or magnitude)
* data2 (y component, or angle measurement)
* measure ('degrees' or 'radians' if you chose mag_ang vector)
 

***
#### physicsObject class
***
   
##### Init Params:
* mass = mass of object in kilograms
* force_vector = the applied force on the object
* static_friction_coefficient = the coefficient of static friction
* kinetic_friction_coefficient = the coefficient of kinetic friction
* starting_velocity = if the object is already moving, this is the velocity

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
