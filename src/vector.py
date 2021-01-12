import math
import random
from src.errors import *


class Vector():
    def __init__(self, vector_type, data1, data2, measure="degrees"):

        # setting values depending on settings
        if vector_type == "mag_ang":
            self.magnitude = data1
            if measure == "degrees":
                self.degrees = data2
                self.radians = math.radians(self.degrees)
            elif measure == "radians":
                self.radians = data2
                self.degrees = math.degrees(self.radians)
            else:
                raise InfoError(f"Measure {measure} is not a valid measurement type (degrees, radians).")

            # creating composite vector
            self.__to_composite_vector()

        # setting values depending on settings
        elif vector_type == "composite":
            self.x = data1
            self.y = data2

            # creating mag_ang vector
            self.__to_mag_ang_vector()

        else:
            raise InfoError(f"Vector type {vector_type} is not a valid vector type (mag_ang, composite")

    def __getitem__(self, item):
        item = item.lower()
        if item == 'x':
            return self.x

        elif item == 'y':
            return self.y

        elif item == 'mag' or item == 'm' or item == 'magnitude':
            return self.magnitude

        elif item == 'rad' or item == 'r' or item == 'radians':
            return self.radians

        elif item == 'deg' or item == 'd' or item == 'degrees':
            return self.degrees

        else:
            raise InfoError("Item option does not exist.")

    def __add__(self, other):
        return Vector("composite", self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector("composite", self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"{[self.x, self.y]}"

    def __to_composite_vector(self):

        # calculates leg distances for vector using m*trig(rad)
        self.x = self.magnitude * math.cos(self.radians)
        self.y = self.magnitude * math.sin(self.radians)

    def __to_mag_ang_vector(self):
        self.radians = math.atan(self.y / self.x)

        if self.x < 0 and self.y > 0:
            self.radians = math.pi + self.radians

        elif self.x < 0 and self.y < 0:
            self.radians = math.pi + self.radians

        elif self.x > 0 and self.y < 0:
            self.radians = 2 * math.pi + self.radians

        self.degrees = math.degrees(self.radians)
        self.magnitude = self.y / math.sin(self.radians)

    @staticmethod
    def dot(v1, v2):
        return v1.x * v2.x + v1.y * v2.y

    @staticmethod
    def generate_random_vector(range1, range2):
        return Vector("composite", random.uniform(*range1), random.uniform(*range2))

    @staticmethod
    def are_coterminal(vec1, vec2):
        return vec1.degrees % 360 == vec2.degrees % 360
