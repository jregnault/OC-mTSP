import argparse
import random
import string

from parser import parseInstance
from solver import Solver

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('instanceA')
    parser.add_argument('instanceB')

    args = parser.parse_args()

    instanceA = parseInstance(args.instanceA)
    instanceB = parseInstance(args.instanceB)

    weightA = random.randint(0,100) / 100
    weightB = random.randint(0,100) / 100

    solver = Solver([instanceA, instanceB], [weightA, weightB])
    solution = solver.solve()
    fitness = solver.fitness(solution)

    psolution = "\n"
    for s in solution:
        psolution += str(s) + " -> "

    pFitness = "\n"
    for f in fitness:
        pFitness += "\t" + str(int(f)) + "\n"

    print("Solution : " + psolution[:-3])
    print("Fitness : " + pFitness)