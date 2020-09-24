from physics import handler

# example of handler class for simple kinematics
obj = handler(A=-10, X0=0, V0=7, T=6.7)
print(obj.values)
# out put = ({'V': -60.0, 'V0': 7, 'X': -177.55, 'X0': 0, 'T': 6.7, 'A': -10}, {'k1': 'V', 'k2': 'X'}) contains values and order of kinematics used to solve

# example of projectile
# from vector = [(what the return value is x,y,projectile),magnitude,angle from horizontal axis]
proj = handler(from_vector=['projectile', 50, 60])
print(proj.values_x)
print(proj.values_y)
proj.graph()
# outputs three graphs, Xyo as a function of time, Xxo as a function of time, and composite function
# also contain kinematic values for both x and y
