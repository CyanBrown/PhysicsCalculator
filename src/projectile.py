import numpy as np
import math
import matplotlib.pyplot as plt
from src.kinematics import kinematics


class projectile:
    ROUND_TO = 3
    GRAPH_FORMATS = {"tx": {"title": "X Position as a Function of Time", "x_label": "Time", "y_label": "X Position"},
                     "ty": {"title": "Y Position as a Function of Time", "x_label": "Time", "y_label": "Y Position"},
                     "xy": {"title": "Y Position as a Function of X Position", "x_label": "X Position",
                            "y_label": "Y Position"}}

    def __init__(self, magnitude, deg_from_x, ykin, measure='deg'):

        kinematics.ROUND_TO = projectile.ROUND_TO

        if ykin['X0'] == None and ykin['X'] == None:
            ykin['X0'] = ykin['X'] = 0
            help = True
        else:
            help = False

        self.y_values = ykin
        self.y_values['A'] = -9.8
        self.x_values = {"X0": 0, "X": None, "A": 0}

        self.measure = measure
        self.deg_from_x = deg_from_x
        self.magnitude = magnitude

        self.__composite_vector()

        if help:
            self.y_values['V'] = -self.y_values['V0']

        self.y_calc = kinematics(self.y_values)
        self.y_values = self.y_calc.values

        self.x_values['T'] = self.y_values['T']
        self.x_calc = kinematics(self.x_values)
        self.x_values = self.x_calc.values

    def __matrix_calc(self, e1, e2, e3):
        eqs = np.array([[e1[0] ** 2, e1[0], 1], [e2[0] ** 2, e2[0], 1], [e3[0] ** 2, e3[0], 1]])
        sols = np.array([[e1[1]], [e2[1]], [e3[1]]])
        vals = np.dot(np.linalg.inv(eqs), sols)
        vals = [vals[0, 0], vals[1, 0], vals[2, 0]]
        formula = str(vals[0]) + "*pow(x,2)+" + str(vals[1]) + "*x+" + str(vals[2])

        return formula

    def __composite_vector(self):
        if self.measure == 'deg':
            vectors = [round(self.magnitude * math.cos(math.radians(self.deg_from_x)), projectile.ROUND_TO),
                       round(self.magnitude * math.sin(math.radians(self.deg_from_x)), projectile.ROUND_TO)]
        elif self.measure == 'rad':
            vectors = [round(self.magnitude * math.cos(self.deg_from_x), projectile.ROUND_TO),
                       round(self.magnitude * math.sin(self.deg_from_x), projectile.ROUND_TO)]

        self.x_values['V0'] = self.x_values['V'] = vectors[0]
        self.y_values['V0'] = vectors[1]

    def __vals_to_time(self, value_to_return):
        dirs = ['x', 'y']
        time = self.y_values['T']

        for t in dirs:
            coords = []
            if t == "y":
                test_vals = self.y_values
                test_vals = kinematics(test_vals).values
            else:
                test_vals = self.x_values
                test_vals = kinematics(test_vals).values

            for i in range(3):
                test_vals['T'] = i
                test_vals[value_to_return] = None
                test_vals = kinematics(test_vals).values

                coords.append([i, test_vals[value_to_return]])

            if t == "y":
                y_form = self.__matrix_calc(coords[0], coords[1], coords[2])
            else:
                x_form = self.__matrix_calc(coords[0], coords[1], coords[2])

        self.y_values['T'] = time
        return (x_form, y_form)

    def __create_all_points(self, x_to, formula):
        x = []
        i = 0
        while i <= x_to:
            x.append(i)
            i += .01

        x = np.array(x)
        y = eval(formula)

        return (x, y)

    def graph(self, style="ty"):

        formula = self.__vals_to_time('X')

        if style == "ty":
            x, y = self.__create_all_points(self.y_values['T'], formula[1])
            plt.plot(x, y)

            plt.title(projectile.GRAPH_FORMATS['ty']['title'])
            plt.xlabel(projectile.GRAPH_FORMATS['ty']['x_label'])
            plt.ylabel(projectile.GRAPH_FORMATS['ty']['y_label'])

        elif style == "tx":
            x, y = self.__create_all_points(self.y_values['T'], formula[0])
            plt.plot(x, y)

            plt.title(projectile.GRAPH_FORMATS['tx']['title'])
            plt.xlabel(projectile.GRAPH_FORMATS['tx']['x_label'])
            plt.ylabel(projectile.GRAPH_FORMATS['tx']['y_label'])

        elif style == "xy":
            x = self.__create_all_points(self.y_values['T'], formula[0])[1]
            y = self.__create_all_points(self.y_values['T'], formula[1])[1]
            plt.plot(x, y)

            plt.title(projectile.GRAPH_FORMATS['xy']['title'])
            plt.xlabel(projectile.GRAPH_FORMATS['xy']['x_label'])
            plt.ylabel(projectile.GRAPH_FORMATS['xy']['y_label'])

        plt.show()