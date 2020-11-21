import math
from src.errors import InfoError
from src.physics import physics
import src.staticPhysics as sP
import matplotlib.pyplot as plt
import numpy as np


class physicsObject():
    # setting class constants
    ROUND_TO = 3
    GRAVITATIONAL_CONSTANT_MAGNITUDE = 9.8
    SCALE_SIZE = 1.1

    def __init__(self, mass, force_vector, static_friction_coefficient=0, kinetic_friction_coefficient=0,
                 measure='deg', starting_velocity=0, vector_type="mag_ang"):
        self.mass = mass
        self.static_friction_coefficient = static_friction_coefficient
        self.kinetic_friction_coefficient = kinetic_friction_coefficient
        self.measure = measure
        self.starting_velocity = starting_velocity
        self.__vector_type = vector_type

        # sets force_vector variable depending on vector type
        if self.__vector_type == "xy":
            force_vector = sP.to_magnitude_angle_vector(force_vector, measure=self.measure)

        elif self.__vector_type != "mag_ang":
            raise InfoError(f"'{self.__vector_type}' is not a valid vector type. Use 'mag_ang' or 'xy'.")

        self.force_vector_magnitude = force_vector[0]
        self.force_vector_deg_from_x = force_vector[1]

        self.__calculate_fb()

    def __calculate_fb(self):
        """

        :return: calculates all the forces acting on the object
        """

        # setting all the forces to the different values
        force_values = sP.to_composite_vector([self.force_vector_magnitude, self.force_vector_deg_from_x])

        # horizontal applied force
        self.Fa = force_values[0]

        # weight = mg = mass*gravitational acceleration
        self.mg = self.mass * -self.GRAVITATIONAL_CONSTANT_MAGNITUDE

        # vertical applied force
        self.Fay = force_values[1]

        # normal force is calculated with mg and the applied force vertical, it can't be negative (in these situations)
        self.Fn = max(round(-self.mg - force_values[1], self.ROUND_TO), 0)

        # calculates theoretical friction
        self.static_friction_max = self.static_friction_coefficient * self.Fn
        self.kinetic_friction = self.kinetic_friction_coefficient * self.Fn

        # determines direction of friction
        if self.Fa >= 0:
            self.static_friction_max *= -1
            self.kinetic_friction *= -1

        # this calculates whether to consider static friction (and how much) or kinetic friction
        if abs(self.Fa) > abs(self.static_friction_max):
            self.actual_friction_force = round(-math.copysign(self.kinetic_friction, self.Fa), self.ROUND_TO)
        else:
            self.actual_friction_force = -math.copysign(abs(self.Fa), self.Fa)

        # calculates acceleration
        self.horizontal_acceleration = round((self.Fa + self.actual_friction_force) / self.mass, self.ROUND_TO)

    def data_at_position(self, position):
        """

        :param position: float, used to find data at point on horizontal axis
        :return: physics object, data at certain position
        """
        obj = physics(V0=self.starting_velocity, A=self.horizontal_acceleration, X0=0, X=position)
        return obj

    def data_at_time(self, time):
        """

        :param time: float, used ot find data at time
        :return: physics object, data at certain time
        """
        obj = physics(V0=self.starting_velocity, A=self.horizontal_acceleration, X0=0, T=time)
        return obj

    def graph_fbd(self, save=False):
        """

        :param save: whether to save the plot
        :return: none
        """

        # setting basic data on graph
        plt.figure()
        plt.plot(0, 0, 'ro', c='black')
        plt.ylabel("Newtons")
        plt.xlabel("Newtons")
        plt.title("Free Body Diagram")

        # changes magnitude deg vector to xy vector
        applied = sP.to_composite_vector([self.force_vector_magnitude, self.force_vector_deg_from_x],
                                         measure=self.measure)

        # calculate dimensions of graph based on vector size
        y_height = max(max(abs(self.Fn), abs(self.mg)), abs(applied[1]))
        x_width = max(abs(applied[0]), abs(self.actual_friction_force))
        square_size = max(x_width, y_height) * self.SCALE_SIZE

        # plotting the vectors
        V = np.array([[0, self.Fn], [0, self.mg], applied, [self.actual_friction_force, 0]])
        plt.plot([0, 0], [-square_size, square_size], linewidth=.5, color='black')
        plt.plot([-square_size, square_size], [0, 0], linewidth=.5, color='black')
        plt.quiver([0, 0, 0, 0], [0, 0, 0, 0], V[:, 0], V[:, 1], angles='xy', scale_units='xy', scale=1,
                   color=['r', 'g', 'b'])

        # saves plot
        if save:
            plt.savefig(f"{str(self)}.jpg")

        # shows plot
        plt.show()

    def __str__(self):
        """

        :return: formated to string statement
        """
        return f"{self.mass}, {[self.force_vector_magnitude, self.force_vector_deg_from_x]}"
