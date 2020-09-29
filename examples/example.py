from src.physics import physics

obj = physics(vector=[60, 60])
print(obj.x_values, obj.y_values)
obj.proj.graph('ty')
obj.proj.graph('tx')
obj.proj.graph('xy')

"""
output
{'X0': 0, 'X': 3.42, 'A': 0, 'V0': 30.0, 'V': 30.0, 'T': 0.114} {'V': -53.082, 'V0': 51.962, 'X': 0, 'X0': 6, 'T': 0.114, 'A': -9.8}
and the images in the folder
"""

kin = physics(V=5, V0=10, T=1.6)
print(kin.values)

"""
output
{'V': 5, 'V0': 10, 'X': 12.0, 'X0': 0, 'T': 1.6, 'A': -3.125}
"""
