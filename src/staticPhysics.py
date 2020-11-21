import math
from src.errors import InfoError
import random

ROUND_TO = 3


def to_composite_vector(vector, measure="deg"):
    """

    :param vector: starting vector
    :return: create V0 for both x and y direction kinematics from vector given in init
    """

    magnitude = vector[0]
    deg_from_x = vector[1]

    # decomposes vector to calculate V0 for both x and y directions
    if measure == 'deg':
        vectors = [round(magnitude * math.cos(math.radians(deg_from_x)), ROUND_TO),
                   round(magnitude * math.sin(math.radians(deg_from_x)), ROUND_TO)]
    elif measure == 'rad':
        vectors = [round(magnitude * math.cos(deg_from_x), ROUND_TO),
                   round(magnitude * math.sin(deg_from_x), ROUND_TO)]

    else:
        raise InfoError(f"{measure} is not a valid value for the parameter 'measure'")

    return vectors


def combine_vector_magnitude_angle(measure="deg", *argsv):
    """

    :param measure: type of angle measure either 'deg' or 'rad' for radians
    :param argsv: the vectors that need to be combined
    :return: the new magnitude degree vector
    """
    vectorx = 0
    vectory = 0

    # convert all vectors to xy vectors to make combination easier
    for vector in argsv:
        decomp_vect = to_composite_vector(vector, measure=measure)

        # adding all vectors together
        vectorx += decomp_vect[0]
        vectory += decomp_vect[1]

    # calculates the deg/rad and magnitude from the the previous values
    if measure == "deg":
        deg_from_x = math.degrees(math.atan(vectory / vectorx))
        if deg_from_x < 0:
            deg_from_x = 180 + deg_from_x
        magnitude = vectory / math.sin(math.radians(deg_from_x))

    elif measure == 'rad':
        deg_from_x = math.atan(vectory / vectorx)
        magnitude = vectory / math.sin(math.radians(deg_from_x))
        if deg_from_x < 0:
            deg_from_x = 2 * math.pi - deg_from_x

    return [round(magnitude, ROUND_TO), round(deg_from_x, ROUND_TO)]


def combine_vector_composition(*argsv):
    """

    :param argsv: all composition vector
    :return: new combined vector
    """

    # adds all vectors together
    vectorx = math.fsum([i[0] for i in argsv])
    vectory = math.fsum([i[1] for i in argsv])

    return [vectorx, vectory]


def to_magnitude_angle_vector(vector, measure="deg"):
    """

    :param vector: xy vector to convert
    :param measure: type of degrees to return
    :return: magnitude degree vector
    :raise InfoError: is measure doesn't exist
    """

    deg_from_x = math.atan(vector[1] / vector[0])
    mag = vector[1] / math.sin(deg_from_x)

    if vector[0] < 0 and vector[1] < 0:
        deg_from_x = 3 * math.pi / 2 + deg_from_x
    elif vector[0] < 0:
        deg_from_x = math.pi + deg_from_x
    elif vector[1] < 0:
        deg_from_x = 2 * math.pi + deg_from_x

    if measure == 'deg':
        return [round(mag, ROUND_TO), round(math.degrees(deg_from_x), ROUND_TO)]
    elif measure == 'rad':
        return [round(mag, ROUND_TO), round(deg_from_x, ROUND_TO)]
    else:
        raise InfoError(f"{measure} is an invalid measure type")


def generate_random_vector(range1=[0, 100], range2=[0, 100]):
    """

    :param range1: list that has range for the first value of the vector
    :param range2: list that has range for the second value of the vector
    :param round_to: rounding number
    :return: random vector
    """
    vector = [round(random.uniform(*range1), ROUND_TO), round(random.uniform(*range2), ROUND_TO)]
    return vector
