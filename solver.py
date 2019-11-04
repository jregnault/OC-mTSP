import random
import numpy as np

class Solver:

    def __init__(self, instances = [], weights = [], solver="random"):
        self.instances = instances
        self.weights = weights
        self.solver = solver
    
    def fitness(self, permutation):
        fitnesses = []
        previous = permutation[0]

        for i in range(0,len(self.weights)):
            fitness = 0
            for p in permutation:
                fitness += self.weights[i] * self.instances[i][previous][p]
                previous = p
            fitnesses.append(fitness)
        
        return fitnesses

    def solve(self):
        permutation = []
        if self.solver == "random":
            choices = np.array(np.arange(0,100,1)).tolist()
            for _ in range(0,100):
                n = random.choice(choices)
                permutation.append(n)
                choices.remove(n)

        return permutation