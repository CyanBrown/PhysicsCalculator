import math
import matplotlib.pyplot as plt
from kinematics import kinematics
import numpy as np
import sys


def matrix_calc(e1, e2, e3):
    eqs = np.array([[e1[0] ** 2, e1[0], 1], [e2[0] ** 2, e2[0], 1], [e3[0] ** 2, e3[0], 1]])
    sols = np.array([[e1[1]], [e2[1]], [e3[1]]])
    vals = np.dot(np.linalg.inv(eqs), sols)
    vals = [vals[0, 0], vals[1, 0], vals[2, 0]]
    formula = str(vals[0]) + "*pow(x,2)+" + str(vals[1]) + "*x+" + str(vals[2])

    return formula


class projectile:
    @staticmethod
    def composite_vector(magnitude, deg_from_horz, measure='deg', round_to=3):
        if measure == 'deg':
            return [round(magnitude * math.cos(math.radians(deg_from_horz)), round_to),
                    round(magnitude * math.sin(math.radians(deg_from_horz)), round_to)]
        elif measure == 'rad':
            return [round(magnitude * math.cos(deg_from_horz), round_to),
                    round(magnitude * math.sin(deg_from_horz), round_to)]

    # @staticmethod
    # def kinematics_points(y_values,x_values):
    #     x_coords = []
    #     y_coords = []
    #     total_length = math.ceil(x_values['X'])
    #     for i in range(0, total_length, .5):
    #         if abs(i) >= abs(values['X']):
    #             y_coords.append(0)
    #             x_coords.append()
    #             return [x_coords,y_coords]
    #
    #         values['X'] = i
    #         kinematics.calculate_attributes(values)

    @staticmethod
    def vals_to_time(v):
        coords = []
        vas = v[0]
        t = vas['T']

        for i in range(3):
            vas['T'] = i
            vas['X'] = None
            y_coord = kinematics.calculate_attributes(vas)[0]['X']
            coords.append([i, y_coord])

        print(coords)
        vas['T'] = t

        formula = matrix_calc(coords[0], coords[1], coords[2])
        print(formula)
        return formula

    @staticmethod
    def graph(formula, x_to=5000, y_l='X', x_l='Time', title='Vertical Distance to Time'):

        x = []
        i = 0
        while i <= x_to:
            x.append(i)
            i += .01
        x = np.array(x)
        y = eval(formula)
        plt.plot(x, y)
        plt.ylabel(y_l)
        plt.xlabel(x_l)
        plt.title(title)
        plt.show()
