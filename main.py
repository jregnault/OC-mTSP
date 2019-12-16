import argparse
import random
import string
import matplotlib.pyplot as plt
import logging
import numpy as np

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

    logging.info("There are %d solutions, with %d dominants (%d comparisons).", len(solutions), len(offlineDominants), solver.comps)

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

    solver.resetTicks()
    onlineDominants = solver.onlineFilter(dominants)
    logging.info("There are %d solutions, with %d dominants (%d comparisons).", len(solutions), len(onlineDominants), solver.comps)

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

    offlineComps = []
    onlineComps = []
    for p in range(1,201):
        logging.info("itération %d", p)
        offComp = 0
        onComp = 0
        for _ in range(0,100):
            solutions = []
            dominants = []
            for _ in range(0,p):
                s = solver.solve()
                solutions.append(s)
                dominants.append(s)
            solver.resetTicks()
            solver.offlineFilter(dominants)
            offComp += solver.comps
            solver.resetTicks()
            solver.onlineFilter(dominants)
            onComp += solver.comps
        offComp /= 100
        onComp /= 100
        offlineComps.append(offComp)
        onlineComps.append(onComp)
    
    p = np.arange(1,201,1)
    plt.plot(p, offlineComps, label="offline filter")
    plt.plot(p, onlineComps, label="online filter")
    plt.xlabel("nombre de solutions générées")
    plt.ylabel("nombre de comparaisons")
    plt.legend()
    plt.title("Nombre de comparaisons en fonctions du nombre de solutions")
    plt.show()
    #psolution = "\n"
    #for s in solution:
    #    psolution += str(s) + " -> "

    #pFitness = "\n"
    #for f in fitness:
    #    pFitness += "\t" + str(int(f)) + "\n"

    #print("Solution : " + psolution[:-3])
    #print("Fitness : " + pFitness)