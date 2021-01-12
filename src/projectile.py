import numpy as np
import math
import matplotlib.pyplot as plt
from src.kinematics import kinematics
from src.errors import *


class projectile:
    GRAVITATIONAL_CONSTANT_MAGNITUDE = 9.8

    # these are the premade graph formats as a dict
    GRAPH_FORMATS = {
        "tx": {"title": "X Position as a Function of Time", "x_label": "Time", "y_label": "X Position"},
        "ty": {"title": "Y Position as a Function of Time", "x_label": "Time", "y_label": "Y Position"},
        "xy": {"title": "Y Position as a Function of X Position", "x_label": "X Position", "y_label": "Y Position"},
        "all": {"title": "Position as a Function of Time", "x_label": "Time", "y_label": "Position"},
    }

    def __init__(self, vector, ykin):
        """

        :param vector: vector of projectile
        :param ykin: y kinematics
        """

        # if default position needs to be set it is set
        if ykin['X0'] == None and ykin['X'] == None:
            ykin['X0'] = ykin['X'] = 0
            help = True
        else:
            help = False

        self.y_values = ykin
        self.y_values['A'] = -projectile.GRAVITATIONAL_CONSTANT_MAGNITUDE
        self.x_values = {"X0": 0, "X": None, "A": 0, 'V0': vector.x, 'V': vector.x}

        self.y_values['V0'] = vector.y

        # if default values were set then V0=V
        if help:
            self.y_values['V'] = -self.y_values['V0']

        self.y_calc = kinematics(self.y_values)
        self.y_values = self.y_calc.values

        self.x_values['T'] = self.y_values['T']
        self.x_calc = kinematics(self.x_values)
        self.x_values = self.x_calc.values

    def __matrix_calc(self, e1, e2, e3):

        """
        :param e1: point example 1 (xpos, ypos)
        :param e2: point example 2 (xpos, ypos)
        :param e3: point example 3 (xpos, ypos)
        :return: str formula of parabola from solvin systems of equations with matrices in ax^2+bx+c form
        """

        eqs = np.array([[e1[0] ** 2, e1[0], 1], [e2[0] ** 2, e2[0], 1], [e3[0] ** 2, e3[0], 1]])
        sols = np.array([[e1[1]], [e2[1]], [e3[1]]])
        vals = np.dot(np.linalg.inv(eqs), sols)
        vals = [vals[0, 0], vals[1, 0], vals[2, 0]]
        formula = str(vals[0]) + "*pow(x,2)+" + str(vals[1]) + "*x+" + str(vals[2])

        return formula

    def __vals_to_time(self, value_to_return):
        """
        :param value_to_return: the kinematic value you want to be on the x axis
        :return: two formulas for x and y to time
        :overview: given two kinematic objects (self.x_values, self.y_values) calculate three points
        """
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

        """
        :param x_to: double the point where the projectile hits X=0
        :param formula: string the formula for the parabola
        :return: all xy coordinates for pyplot to graph
        """

        x = []
        i = 0
        while i <= x_to:
            x.append(i)
            i += .01

        x = np.array(x)
        y = eval(formula)

        return (x, y)

    def graph(self, style="ty", save=False):

        """
        :param style: str style of graph to judge which values it calculates and what the labels are
        :param save: bool True to save the image as a jpg
        :return: print images
        """

        formula = self.__vals_to_time('X')

        try:
            plt.title(projectile.GRAPH_FORMATS[style]['title'])
            plt.xlabel(projectile.GRAPH_FORMATS[style]['x_label'])
            plt.ylabel(projectile.GRAPH_FORMATS[style]['y_label'])
        except:
            raise graphError(
                f'Graph style "{style}", does not exist or is not fully initialized, you can add new styles by adding '
                f'to projectiles.GRAPH_FORMATS')

        if style == "ty":
            x, y = self.__create_all_points(self.y_values['T'], formula[1])
            plt.plot(x, y)

        elif style == "tx":
            x, y = self.__create_all_points(self.y_values['T'], formula[0])
            plt.plot(x, y)

        elif style == "xy":
            x = self.__create_all_points(self.y_values['T'], formula[0])[1]
            y = self.__create_all_points(self.y_values['T'], formula[1])[1]
            plt.plot(x, y)

        elif style == "all":

            x, y = self.__create_all_points(self.y_values['T'], formula[1])
            plt.plot(x, y)

            x, y = self.__create_all_points(self.y_values['T'], formula[0])
            plt.plot(x, y)

        if save:
            plt.savefig(f"{style}.jpg")

        plt.show()
