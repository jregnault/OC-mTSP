import argparse
import random
import string
import matplotlib.pyplot as plt
import logging

from parser import parseInstance
from solver import Solver

if __name__ == "__main__":

    logging.basicConfig(
        format='[%(asctime)s][%(levelname)s] %(message)s',
        level=logging.INFO,
        datefmt="%d-%m-%Y %H:%M:%S"
    )

    parser = argparse.ArgumentParser()
    parser.add_argument('instanceA')
    parser.add_argument('instanceB')

    args = parser.parse_args()

    instanceA = parseInstance(args.instanceA)
    instanceB = parseInstance(args.instanceB)

    weightA = random.randint(0,100) / 100
    weightB = random.randint(0,100) / 100

    solver = Solver([instanceA, instanceB], [weightA, weightB])
    solutions = []
    dominants = []
    for _ in range(0,500):
        s = solver.solve()
        solutions.append(s)
        dominants.append(s)

    offlineDominants = solver.offlineFilter(dominants)

    logging.info("There are %d solutions, with %d dominants.", len(solutions), len(offlineDominants))

    offSX = []
    offSY = []
    offX = []
    offY = []
    for d in solutions:
        if d in offlineDominants:
            offX.append(solver.fitness(d)[0])
            offY.append(solver.fitness(d)[1])
        else:
            offSX.append(solver.fitness(d)[0])
            offSY.append(solver.fitness(d)[1])

    plt.plot(offSX, offSY, "xb")
    plt.plot(offX, offY, 'xr')
    
    plt.xlabel(args.instanceA[16])
    plt.ylabel(args.instanceB[16])

    plt.title("Front Pareto calculé avec un filtre offline")
    plt.show()

    onlineDominants = solver.onlineFilter(dominants)
    logging.info("There are %d solutions, with %d dominants.", len(solutions), len(onlineDominants))

    offSX = []
    offSY = []
    offX = []
    offY = []
    for d in solutions:
        if d in onlineDominants:
            offX.append(solver.fitness(d)[0])
            offY.append(solver.fitness(d)[1])
        else:
            offSX.append(solver.fitness(d)[0])
            offSY.append(solver.fitness(d)[1])

    plt.plot(offSX, offSY, "xb")
    plt.plot(offX, offY, 'xr')
    
    plt.xlabel(args.instanceA[16])
    plt.ylabel(args.instanceB[16])

    plt.title("Front Pareto calculé avec un filtre online")
    plt.show()

    #psolution = "\n"
    #for s in solution:
    #    psolution += str(s) + " -> "

    #pFitness = "\n"
    #for f in fitness:
    #    pFitness += "\t" + str(int(f)) + "\n"

    #print("Solution : " + psolution[:-3])
    #print("Fitness : " + pFitness)