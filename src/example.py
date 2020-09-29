from src.physics import physics

obj = physics(vector=[60, 60])
print(obj.x_values, obj.y_values)
obj.proj.graph('ty')
obj.proj.graph('tx')
obj.proj.graph('xy')
