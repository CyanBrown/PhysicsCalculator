import math
from src.errors import *


class kinematics:

    def __init__(self, kinvalues):
        """
        :param kinvalues: dictionary of known values, used keys = ['X','X0','V','V0','A','T']
        """
        self.values = kinvalues
        self.solved = False

        # calls calculate attributes to start the calculations
        self.__caluclate_attributes()

    def __kinematicOne(self):

        # makes sure there is only 1 unknown variable
        elements = [self.values['V0'], self.values['V'], self.values['A'], self.values['T']]
        unknown_variables = elements.count(None)

        # calculates unknown variable
        if unknown_variables == 1:
            if self.values['V0'] is None:
                self.values['V0'] = float(-(-self.values['V'] + (self.values['A'] * self.values['T'])))

            elif self.values['V'] is None:
                self.values['V'] = float(self.values['V0'] + (self.values['A'] * self.values['T']))

            elif self.values['A'] is None:
                self.values['A'] = float((self.values['V'] - self.values['V0']) / self.values['T'])

            elif self.values['T'] is None:
                self.values['T'] = float((self.values['V'] - self.values['V0']) / self.values['A'])

    def __kinematicTwo(self):

        # makes sure there is only 1 unknown variable
        elements = [self.values['X'], self.values['X0'], self.values['V0'], self.values['A'], self.values['T']]
        unknown_variables = elements.count(None)

        # calculates unknown variable
        if unknown_variables == 1:
            if self.values['X'] is None:
                self.values['X'] = float(
                    self.values['X0'] + self.values['V0'] * self.values['T'] + .5 * self.values['A'] * (
                            self.values['T'] ** 2))

            elif self.values['X0'] is None:
                self.values['X0'] = float(-(
                        -self.values['X'] + self.values['V0'] * self.values['T'] + .5 * self.values['A'] * (
                        self.values['T'] ** 2)))

            elif self.values['V0'] is None:
                self.values['V0'] = float(
                    (self.values['X'] - self.values['X0'] - .5 * self.values['A'] * (self.values['T'] ** 2)) /
                    self.values['T'])

            elif self.values['A'] is None:
                self.values['A'] = float(
                    (self.values['X'] - self.values['X0'] - self.values['V0'] * self.values['T']) / (
                            .5 * (self.values['T'] ** 2)))

    def __kinematicThree(self):

        # makes sure there is only 1 unknown variable
        elements = [self.values['V'], self.values['V0'], self.values['X0'], self.values['A'], self.values['X']]
        unknown_variables = elements.count(None)

        # calculates unknown variable
        if unknown_variables == 1:
            if self.values['V'] == None:
                self.values['V'] = float(
                    math.sqrt(self.values['V0'] ** 2 + 2 * self.values['A'] * (self.values['X'] - self.values['X0'])))

    def __caluclate_attributes(self):
        count_none = sum(value == None for value in self.values.values())

        # loop through the three kinematics calculations until it solves
        while count_none > 0:
            # solved stat is determined by amount of time none occurs
            count_none = sum(value == None for value in self.values.values())

            # calls all the kinematic functions
            self.__kinematicOne()
            self.__kinematicTwo()
            self.__kinematicThree()

            # if the values given is unsolvable and we don't have any position we set the default position to 0
            check_none = sum(value == None for value in self.values.values())
            if count_none == check_none:
                if self.values['X0'] is None and (self.values['X'] is None or self.values['A'] is None):
                    self.values['X0'] = 0
                elif self.values['V0'] is None and self.values['V'] is None:
                    self.values["V0"] = 0
                else:
                    # we break if there is already a position
                    if self.values['T'] < 0:
                        self.values['T'] = -self.values['T']
                        self.values['V'] = -self.values['V']

                    break
