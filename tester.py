from kinematics import kinematics
from projectile import projectile, matrix_calc
import matplotlib.pyplot as plt
from physics import handler

# obj = Physics(X=15,X0=0,T=5,V0=10.5)
#
# print(obj.values)

# print(handle(X0=0,T=5,A=0,from_vector=['x',24,40]))
obj = handler(A=-10, X0=0, V0=7, T=6.7)
print(obj.values)

# print(kinematics.calculate_attributes({'X0':0,'X':500,'V0':0,'T':2,'V':None,'A':None}))
#
# def g2():
#     for q in range(0, 90, 5):
#         kin = handler(from_vector=['projectile', q, q], X0=100)
#         kin.values_y[0]['T'] *= 2
#         x_vals, y_vals = projectile.y_vals_to_time(kin.values_y)
#         print(x_vals,y_vals)
#         plt.plot(x_vals, y_vals)
#     plt.show()
#
# g2()
# formula = matrix_calc([0,0],[2,4],[4,16])
# print(formula)
# projectile.graph(formula,x_to=4)

# x=20
# print(eval('2.0*pow(x,2)+-8.0*x+9.0'))
