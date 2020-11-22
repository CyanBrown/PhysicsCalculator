from src.physics import physics
from src.physicsObject import physicsObject
import src.staticPhysics as sp

# projectile calculations
obj = physics(vector=[60, 60])
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
obj = physicsObject(15, [100, 35], static_friction_coefficient=.5, kinetic_friction_coefficient=.3)
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

# static physics functions - set to default degree
starting_mag_deg_vector = sp.generate_random_vector(range1=[100, 150], range2=[0, 360])
print(starting_mag_deg_vector)

converted_xy_vector = sp.to_composite_vector(starting_mag_deg_vector)
print(converted_xy_vector)

converted_mag_deg_vector = sp.to_magnitude_degree_angle(converted_xy_vector)
print(converted_mag_deg_vector)

vectors = [sp.generate_random_vector(range1=[100, 150], range2=[0, 360]) for _ in range(0, 5)]
print(vectors)
combined_vector = sp.combine_vector_composition(*vectors)
print(combined_vector)
mag_deg_combined_vector = sp.combine_vector_magnitude_angle("deg", *vectors)
print(mag_deg_combined_vector)

"""
example output:

[115.315, 203.673]
[-105.611, -46.301]
[-115.315, 293.673]

[[140.596, 234.598], [143.649, 81.223], [121.888, 48.434], [139.742, 284.725], [101.161, 28.145]]
[647.0360000000001, 677.125]
[149.34, 12.031]
"""
