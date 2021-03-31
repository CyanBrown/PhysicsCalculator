from tests.kinematicsTester import tester as ktest
from tests.vectorTester import tester as vtest

working = ktest() and vtest()
work = {True: "SUCCESS", False: "FAILURE"}

print(f"\nFinal Testing Status: {work[working]}")
