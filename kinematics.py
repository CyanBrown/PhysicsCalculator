import math


def occurances(lst, e):
    count = 0
    for i in lst:
        if i == e:
            count += 1

    return count


class kinematics:
    order = {}

    def __init__(self, X=None, X0=None, V=None, V0=None, A=None, T=None, round_to=3):
        self.values = {'X': X, 'X0': X0, 'V': V, 'V0': V0, 'A': A, 'T': T}
        self.has_all_vals = False
        self.round_to = round_to
        self.order = {}
        self.__calculate_attributes()

    def __kinematic1(self):
        # V = V0+AT
        self.elements_k1 = [self.values['V0'], self.values['V'], self.values['A'], self.values['T']]

        if occurances(self.elements_k1, None) > 1:
            return None

        if self.values['V'] == None:
            return {'V': round(float(self.values['V0'] + (self.values['A'] * self.values['T'])), self.round_to)}
        elif self.values['V0'] == None:
            return {'V0': round(float(-(-self.values['V'] + (self.values['A'] * self.values['T']))), self.round_to)}
        elif self.values['A'] == None:
            return {'A': round(float((self.values['V'] - self.values['V0']) / self.values['T']), self.round_to)}
        elif self.values['T'] == None:
            return {'T': round(float((self.values['V'] - self.values['V0']) / self.values['A']), self.round_to)}

    def __kinematic2(self):
        # X = X0+V0(T)+.5(A)(T)^2

        self.elements_k2 = [self.values['X'], self.values['X0'], self.values['V0'], self.values['A'], self.values['T']]

        if occurances(self.elements_k2, None) > 1:
            return None

        if self.values['X'] == None:
            return {'X': round(float(
                self.values['X0'] + self.values['V0'] * self.values['T'] + .5 * self.values['A'] * (
                        self.values['T'] ** 2)), self.round_to)}
        elif self.values['X0'] == None:
            return {'X0': round(float(-(
                    -self.values['X'] + self.values['V0'] * self.values['T'] + .5 * self.values['A'] * (
                    self.values['T'] ** 2))), self.round_to)}
        elif self.values['V0'] == None:
            kinematics.order['k2'] = 'V0'
            return {'V0': round(float(
                (self.values['X'] - self.values['X0'] - .5 * self.values['A'] * (self.values['T'] ** 2)) / self.values[
                    'T']), self.round_to)}
        elif self.values['A'] == None:
            kinematics.order['k2'] = 'A'
            return {'A': round(float((self.values['X'] - self.values['X0'] - self.values['V0'] * self.values['T']) / (
                    .5 * (self.values['T'] ** 2))), self.round_to)}

    def __kinematic3(self):
        # V^2 = V0^2 +2(A)(X-X0)

        self.elements_k3 = [self.values['V'], self.values['V0'], self.values['X0'], self.values['A'], self.values['X']]

        if occurances(self.elements_k3, None) > 1:
            return None

        if self.values['V'] == None:
            return {'V': round(float(
                math.sqrt(self.values['V0'] ** 2 + 2 * self.values['A'] * (self.values['X'] - self.values['X0']))),
                self.round_to)}

    def __calculate_attributes(self):

        while (p := occurances(self.values.values(), None)) > 0:

            self.count_wrong = 0
            if p == 2 and self.values["X0"] == None and self.values["X"] == None:
                self.values["X0"] = 0

            self.i = self.kinematic1(V0=self.values['V0'], V=self.values['V'], A=self.values['A'], T=self.values['T'],
                                     round_to=self.round_to)
            if self.i != None:
                self.values[[t for t in self.i.keys()][0]] = [q for q in self.i.values()][0]
            else:
                self.count_wrong += 1
            self.i = self.kinematic2(X=self.values['X'], X0=self.values['X0'], V0=self.values['V0'], A=self.values['A'],
                                     T=self.values['T'])
            if self.i != None:
                self.values[[t for t in self.i.keys()][0]] = [q for q in self.i.values()][0]
            else:
                self.count_wrong += 1
            self.i = self.kinematic3(X=self.values['X'], X0=self.values['X0'], V0=self.values['V0'], A=self.values['A'],
                                     V=self.values['T'])
            if self.i != None:
                self.values[[t for t in self.i.keys()][0]] = [q for q in self.i.values()][0]

            else:
                self.count_wrong += 1

            if self.count_wrong >= 3:
                if p == 2 and self.values["X0"] == None and self.values["X"] == None:
                    self.values["X0"] = 0

                else:
                    self.has_all_vals = False
                    break

        if None not in self.values.values() and self.values['T'] / -self.values['T'] == -1:
            self.values['T'] = -self.values['T']
            self.values['V'] = -self.values['V']

    @staticmethod
    def kinematic1(V0=None, V=None, A=None, T=None, round_to=3):
        # V = V0+AT
        elements_k1 = [V0, V, A, T]
        if occurances(elements_k1, None) > 1:
            return None

        if V == None:
            kinematics.order['k1'] = 'V'
            return {'V': round(float(V0 + (A * T)), round_to)}
        elif V0 == None:
            kinematics.order['k1'] = 'V0'
            return {'V0': round(float(-(-V + (A * T))), round_to)}
        elif A == None:
            kinematics.order['k1'] = 'A'
            return {'A': round(float((V - V0) / T), round_to)}
        elif T == None:
            kinematics.order['k1'] = 'T'
            return {'T': round(float((V - V0) / A), round_to)}

    @staticmethod
    def kinematic2(X=None, X0=None, V0=None, A=None, T=None, round_to=3):
        # X = X0+V0(T)+.5(A)(T)^2
        elements_k2 = [X, X0, V0, A, T]

        if occurances(elements_k2, None) > 1:
            return None

        if X == None:
            kinematics.order['k2'] = 'X'
            return {'X': round(float(X0 + V0 * T + .5 * A * (T ** 2)), round_to)}
        elif X0 == None:
            kinematics.order['k2'] = 'X0'
            return {'X0': round(float(-(-X + V0 * T + .5 * A * (T ** 2))), round_to)}
        elif V0 == None:
            kinematics.order['k2'] = 'V0'
            return {'V0': round(float((X - X0 - .5 * A * (T ** 2)) / T), round_to)}
        elif A == None:
            kinematics.order['k2'] = 'A'
            return {'A': round(float((X - X0 - V0 * T) / (.5 * (T ** 2))), round_to)}

    @staticmethod
    def kinematic3(V=None, V0=None, A=None, X=None, X0=None, round_to=3):
        # V^2 = V0^2 +2(A)(X-X0)
        elements_k3 = [V, V0, X0, A, X]

        if occurances(elements_k3, None) > 1:
            return None

        if V == None:
            kinematics.order['k3'] = 'V'
            return {'V': round(float(math.sqrt(V0 ** 2 + 2 * A * (X - X0))), round_to)}
        # elif A == None:
        #     kinematics.order['k3'] = 'A'
        #     return {'A': round(float((V ** 2 - V0 ** 2) / (2 * (X - X0))), round_to)}

    @staticmethod
    def calculate_attributes(value, round_to=3):

        values = value
        while (p := occurances(values.values(), None)) > 0:
            count_wrong = 0
            if p == 2 and values["X0"] == None and values["X"] == None:
                values["X0"] = 0

            i = kinematics.kinematic1(V0=values['V0'], V=values['V'], A=values['A'], T=values['T'], round_to=round_to)
            if i != None:
                values[[t for t in i.keys()][0]] = [q for q in i.values()][0]
            else:
                count_wrong += 1
            i = kinematics.kinematic2(X=values['X'], X0=values['X0'], V0=values['V0'], A=values['A'], T=values['T'])
            if i != None:
                values[[t for t in i.keys()][0]] = [q for q in i.values()][0]
            else:
                count_wrong += 1
            i = kinematics.kinematic3(X=values['X'], X0=values['X0'], V0=values['V0'], A=values['A'], V=values['V'])
            if i != None:
                values[[t for t in i.keys()][0]] = [q for q in i.values()][0]
            else:
                count_wrong += 1

            if occurances(values.values(), None) == 0:
                return (values, kinematics.order)

            if count_wrong >= 3:
                if p == 2 and values["X0"] == None and values["X"] == None:
                    values["X0"] = 0

                else:
                    break

        if None not in values.values() and values['T'] < 0:
            values['T'] = -values['T']
            values['V'] = -values['V']
        return (values, kinematics.order)
