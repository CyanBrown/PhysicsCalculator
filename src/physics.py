from src.kinematics import kinematics
from src.projectile import projectile

class physics:
    GRAVATATIONAL_CONSTANT_MAGNITUDE = 9.8

    def __init__(self, V=None, V0=None, X=None, X0=None, T=None, A=None, vector=None, round_to=3, measure='deg'):

        """
        :param V: velocity final
        :param V0: velocity initial
        :param X: position final
        :param X0: position initial
        :param T: total time
        :param A: acceleration
        :param vector: list [magnitude,degrees or radians from x axis]
        :param round_to: decimal places to round to
        :param measure: weather or not you used deg or rad in vector
        """

        projectile.ROUND_TO = round_to
        kinematics.ROUND_TO = round_to
        projectile.GRAVATATIONAL_CONSTANT_MAGNITUDE = physics.GRAVATATIONAL_CONSTANT_MAGNITUDE

        self.values = {"V": V, "V0": V0, "X": X, "X0": X0, "T": T, "A": A}
        self.round_to = round_to

        if vector != None:
            self.use_vector = True
            self.vector = vector
            self.measure = measure
        else:
            self.use_vector = False

        self.__calculate()

    def __calculate(self):

        # calculates vectors and kinematics depending on which one appears in init

        if self.use_vector:
            self.proj = projectile(self.vector[0], self.vector[1], self.values, measure=self.measure)
            self.x_values = self.proj.x_values
            self.y_values = self.proj.y_values
            del self.values

        else:
            vCalc = kinematics(self.values)
            self.values = vCalc.values
