from src.physics import physics


def num_is_equal(n1, n2):
    return round(n1, 5) == round(n2, 5)


def dict_is_equal(d1, d2):
    for i in d1.keys():
        if not num_is_equal(d1[i], d2[i]):
            return False

    return True


problem_set = [
    {"A": 3.2, "T": 32.8, "ans": {"V0": 0, "V": 104.96, "X0": 0, "X": 1721.344, "A": 3.2, "T": 32.8}},
    {"X": 110, "T": 5.21, "V0": 0, "ans": {"A": 8.104892039, "V0": 0, "V": 42.22648752, "X0": 0, "X": 110, "T": 5.21}},
    {"A": -9.8, "T": 2.6, "V0": 0, "ans": {'V0': 0, "V": -25.48, "X0": 0, "X": -33.124, "A": -9.8, "T": 2.6}},
    {"V0": 18.5, "V": 46.1, "T": 2.47,
     'ans': {"A": 11.17408907, "T": 2.47, "V0": 18.5, "V": 46.1, "X0": 0, "X": 79.781}},
    {'V0': 0, "X0": 1, "X": -.4, "A": -1.67,
     'ans': {"X0": 1, "X": -.4, "V0": 0, "A": -1.67, "T": 1.294853933, "V": -2.162406068}}
]


def tester():
    print("\nKINEMATICS\n")
    working = True
    for i in problem_set:
        phy = physics(A=i.get("A"), V=i.get('V'), V0=i.get('V0'), X0=i.get("X0"), X=i.get("X"), T=i.get('T'))

        if dict_is_equal(phy.values, i['ans']):
            print(f"Set {problem_set.index(i)}: SUCCESS")

        else:
            print(f"Set {problem_set.index(i)}: FAILURE\nReal: {i['ans']},\nGiven: {phy.values}")
            working = False

    return working
