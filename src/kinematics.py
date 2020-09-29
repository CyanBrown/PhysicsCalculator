import math

def occurances(lst, e):
    count = 0
    for i in lst:
        if i == e:
            count += 1

    return count

class kinematics:
    ROUND_TO = 3

    def __init__(self, kinvalues):
        self.values = kinvalues

        self.__caluclate_attributes()

    def __kinematicOne(self):
        elements = [self.values['V0'], self.values['V'], self.values['A'], self.values['T']]
        unknown_variables = occurances(elements, None)

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
        elements = [self.values['X'], self.values['X0'], self.values['V0'], self.values['A'], self.values['T']]
        unknown_variables = occurances(elements, None)

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
        elements = [self.values['V'], self.values['V0'], self.values['X0'], self.values['A'], self.values['X']]
        unknown_variables = occurances(elements, None)

        if unknown_variables == 1:
            if self.values['V'] == None:
                self.values['V'] = round(float(
                    math.sqrt(self.values['V0'] ** 2 + 2 * self.values['A'] * (self.values['X'] - self.values['X0']))),
                                         kinematics.ROUND_TO)

    def __caluclate_attributes(self):
        count_none = occurances(self.values.values(), None)

        while count_none > 0:
            count_none = occurances(self.values.values(), None)

            self.__kinematicOne()
            self.__kinematicTwo()
            self.__kinematicThree()

            check_none = occurances(self.values.values(), None)
            if count_none == check_none:
                if self.values['X'] == None and self.values['X0'] == None:
                    self.values['X0'] = 0
                else:
                    break

        if self.values['T'] < 0:
            self.values['T'] = -self.values['T']
            self.values['V'] = -self.values['V']
