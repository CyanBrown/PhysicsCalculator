from src.physics import physics
from oldCode.oldPhysics import handler

# test = handler(from_vector=['projectile',60,60],X0=0,X=0,A=-9.8)
# print(test.values)

# example of handler class for simple kinematics

obj = physics(vector=[60, 60])
print(obj.x_values, obj.y_values)
obj.proj.graph()
# out put = ({'V': -60.0, 'V0': 7, 'X': -177.55, 'X0': 0, 'T': 6.7, 'A': -10}, {'k1': 'V', 'k2': 'X'}) contains values and order of kinematics used to solve

# example of projectile
# from vector = [(what the return value is x,y,projectile),magnitude,angle from horizontal axis]
# proj = handler(from_vector=['projectile', 50, 60])
# print(proj.values_x)
# print(proj.values_y)
# proj.graph()
# outputs three graphs, Xyo as a function of time, Xxo as a function of time, and composite function
# also contain kinematic values for both x and y
