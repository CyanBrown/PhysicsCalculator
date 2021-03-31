from src.vector import Vector
import math


def nums_are_equal(n1, n2, accuracy=2, ignore_sign=False):
    if not ignore_sign:
        return round(n1, accuracy) == round(n2, accuracy)
    else:
        n2 = math.copysign(n2, n1)
        return round(n1, accuracy) == round(n2, accuracy)


def tester():
    working = True

    composite_to_mag = [
        {"given": [15, 25], "expected": [29.15475947, 1.030376827, 59.03624347]},
        {"given": [-36, 18], "expected": [40.24922356, 2.677945045, 153.43494884685]},
        {"given": [-42, -69], "expected": [80.77747211, 4.165600139, 238.6715071]},
        {'given': [13, -26], "expected": [29.06888371, 5.176036589, 296.5650512]}
    ]

    mag_to_composite = [
        {'given': [35, 74, "degrees"], "expected": [9.647307454, 33.64415936, 1.29154]},
        {'given': [69, 123, "degrees"], "expected": [-37.58009342, 57.86826919, 2.14675]},
        {'given': [42, 186, "degrees"], "expected": [-41.76991961, -4.390195457, 3.24631]},
        {'given': [15, 346, "degrees"], "expected": [14.55443589, -3.628828434, 6.03884]},
        {'given': [35, 1.29154, "radians"], "expected": [9.647307454, 33.64415936, 74]},
        {'given': [69, 2.14675, "radians"], "expected": [-37.58009342, 57.86826919, 123]},
        {'given': [42, 3.24631, "radians"], "expected": [-41.76991961, -4.390195457, 186]},
        {'given': [15, 6.03884, "radians"], "expected": [14.55443589, -3.628828434, 346]}
    ]

    print("\nVector Conversion Test (Composite => Mag_ang)\n")
    for i in composite_to_mag:
        obj = Vector("composite", *i['given'])
        if nums_are_equal(obj.magnitude, i['expected'][0]) and nums_are_equal(obj.radians,
                                                                              i['expected'][1]) and nums_are_equal(
                obj.degrees, i['expected'][2]):
            print(f"Conversion {composite_to_mag.index(i)}: SUCCESS")

        else:
            working = False
            print(f"Conversion {composite_to_mag.index(i)}: FAILURE")
            print(f"Expected: {i['expected']},\nReceived: {obj.magnitude, obj.radians, obj.degrees}")

    print("\nVector Conversion Test (Mag_ang => Composite)\n")
    for i in mag_to_composite:
        obj = Vector('mag_ang', *i['given'])

        if nums_are_equal(obj.x, i['expected'][0]) and nums_are_equal(obj.y, i['expected'][1]) and (
                nums_are_equal(obj.degrees, i['expected'][2]) or nums_are_equal(obj.radians, i['expected'][2])):
            print(f"Conversion {mag_to_composite.index(i)}: SUCCESS")

        else:
            working = False
            print(f"Conversion {mag_to_composite.index(i)}: FAILURE")
            print(f"Expected: {i['expected']},\nReceived: {obj.x, obj.y, obj.degrees, obj.radians}")

    return working
