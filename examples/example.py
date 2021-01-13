from src.physics import physics
from src.physicsObject import physicsObject
from src.vector import Vector

# projectile calculations
obj = physics(vector=Vector('mag_ang', 50, 50))
print(obj.x_values, obj.y_values)
obj.proj.graph('all')
obj.proj.graph('ty')
obj.proj.graph('tx')
obj.proj.graph('xy')

"""
output
{'X0': 0, 'X': 3.42, 'A': 0, 'V0': 30.0, 'V': 30.0, 'T': 0.114} {'V': -53.082, 'V0': 51.962, 'X': 0, 'X0': 6, 'T': 0.114,'A': -9.8}
and the images in the folder
"""

# kinematics calculations
kin = physics(V=5, V0=10, T=1.6)
print(kin.values)

"""
output
{'V': 5, 'V0': 10, 'X': 12.0, 'X0': 0, 'T': 1.6, 'A': -3.125}
"""

# forces calculations
obj = physicsObject(15, Vector('composite', 100, 35), static_friction_coefficient=.5, kinetic_friction_coefficient=.3)
print(obj)
obj.graph_fbd()

values_at_pos = obj.data_at_position(50)
print(values_at_pos.values)

values_at_time = obj.data_at_time(13)
print(values_at_time.values)

"""
output

the graph named "15, [100,35].jpg"

15, [100, 35]
{'V': 19.152, 'V0': 0, 'X': 50, 'X0': 0, 'T': 5.221, 'A': 3.668}
{'V': 47.684, 'V0': 0, 'X': 309.946, 'X0': 0, 'T': 13, 'A': 3.668}
"""

vect1 = Vector('mag_ang', 150, 125)
vect2 = Vector('composite', -30, -10)

print(vect1, vect2)

# adding and subtracting vectors
print(vect1 + vect2)
print(vect1 - vect2)

# dot product
print(Vector.dot(vect1, vect2))

# random vector
print(Vector.generate_random_vector([0, 150], [0, 150]))

# checks if vector angles are coterminal
print(Vector.are_coterminal(vect1, vect2))

"""
Output:

Vectors
[-86.03646545265693, 122.87280664334875] [-30, -10]

Added
[-116.03646545265693, 112.87280664334875]

Subtracted
[-56.03646545265693, 132.87280664334875]

Dot Product
1352.36589714622

Random Vector
[98.67982302632979, 31.80723462751877]

Are Coterminal
False
"""
