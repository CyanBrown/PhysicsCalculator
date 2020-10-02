import math
from src.errors import *


# counts amount of time e is in lst
# used for checking if variable is none
def occurances(lst, e):
    """ 
    :param lst: list you want to count through
    :param e: value you are looking for
    :return count: count of e in lst
    """
    count = 0
    for i in lst:
        if i == e:
            count += 1

    return count


class kinematics:
    ROUND_TO = 3

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
        unknown_variables = occurances(elements, None)

        # calculates unknown variable
        if unknown_variables == 1:
            if self.values['V0'] == None:
                self.values['V0'] = round(float(-(-self.values['V'] + (self.values['A'] * self.values['T']))),
                                          kinematics.ROUND_TO)
            elif self.values['V'] == None:
                self.values['V'] = round(float(self.values['V0'] + (self.values['A'] * self.values['T'])),
                                         kinematics.ROUND_TO)
            elif self.values['A'] == None:
                self.values['A'] = round(float((self.values['V'] - self.values['V0']) / self.values['T']),
                                         kinematics.ROUND_TO)
            elif self.values['T'] == None:
                self.values['T'] = round(float((self.values['V'] - self.values['V0']) / self.values['A']),
                                         kinematics.ROUND_TO)

    def __kinematicTwo(self):

        # makes sure there is only 1 unknown variable
        elements = [self.values['X'], self.values['X0'], self.values['V0'], self.values['A'], self.values['T']]
        unknown_variables = occurances(elements, None)

        # calculates unknown variable
        if unknown_variables == 1:
            if self.values['X'] == None:
                self.values['X'] = round(float(
                    self.values['X0'] + self.values['V0'] * self.values['T'] + .5 * self.values['A'] * (
                            self.values['T'] ** 2)), kinematics.ROUND_TO)
            elif self.values['X0'] == None:
                self.values['X0'] = round(float(-(
                        -self.values['X'] + self.values['V0'] * self.values['T'] + .5 * self.values['A'] * (
                        self.values['T'] ** 2))), kinematics.ROUND_TO)
            elif self.values['V0'] == None:
                self.values['V0'] = round(float(
                    (self.values['X'] - self.values['X0'] - .5 * self.values['A'] * (self.values['T'] ** 2)) /
                    self.values['T']), kinematics.ROUND_TO)
            elif self.values['A'] == None:
                self.values['A'] = round(float(
                    (self.values['X'] - self.values['X0'] - self.values['V0'] * self.values['T']) / (
                            .5 * (self.values['T'] ** 2))), kinematics.ROUND_TO)

    def __kinematicThree(self):

        # makes sure there is only 1 unknown variable
        elements = [self.values['V'], self.values['V0'], self.values['X0'], self.values['A'], self.values['X']]
        unknown_variables = occurances(elements, None)

        # calculates unknown variable
        if unknown_variables == 1:
            if self.values['V'] == None:
                self.values['V'] = round(float(
                    math.sqrt(self.values['V0'] ** 2 + 2 * self.values['A'] * (self.values['X'] - self.values['X0']))),
                    kinematics.ROUND_TO)

    def __caluclate_attributes(self):
        count_none = occurances(self.values.values(), None)

        # loop through the three kinematics calculations until it solves
        while count_none > 0:
            # solved stat is determined by amount of time none occurs
            count_none = occurances(self.values.values(), None)

            # calls all the kinematic functions
            self.__kinematicOne()
            self.__kinematicTwo()
            self.__kinematicThree()

            # if the values given is unsolvable and we don't have any position we set the default position to 0
            check_none = occurances(self.values.values(), None)
            if count_none == check_none:
                if self.values['X'] == None and self.values['X0'] == None:
                    self.values['X0'] = 0
                else:
                    # we break if there is already a position
                    break

        else:
            self.solved = True

        if self.solved:
            # makes sure there is no negative time return
            if self.values['T'] < 0:
                self.values['T'] = -self.values['T']
                self.values['V'] = -self.values['V']
