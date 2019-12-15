import random
import numpy as np
import logging

class Solver:

    def __init__(self, instances = [], weights = [], solver="random"):
        self.instances = instances
        self.weights = weights
        self.solver = solver
    
    def fitness(self, permutation):
        """Computes the fitness for every objective in the permutation
        Input:
        ------
        - permutation : the solution to test

        Output: an array containing the fitness of every objective in the permutation.
        """
        fitnesses = []
        previous = permutation[0]

        for i in range(0,len(self.weights)):
            fitness = 0
            for p in permutation:
                fitness += self.weights[i] * self.instances[i][previous[i]][p[i]]
                previous = p
            fitnesses.append(fitness)
        
        return fitnesses

    def solve(self):
        permutation = []
        choices = []
        if self.solver == "random":
            for _ in self.instances:
                choices.append(np.array(np.arange(0,100,1)).tolist())
            for _ in range(0,100):
                point = []
                for c in choices:
                    n = random.choice(c)
                    point.append(n)
                    c.remove(n)
                permutation.append(point)

        return permutation
    
    def dominates(self, fitA, fitB):
        return (fitA[0] < fitB[0]) and (fitA[1] < fitB[1])
    
    def getDominants(self, solutions):
        dominants = solutions
        
        for s in solutions:
            if s in dominants:
                rejected = []
                a = self.fitness(s)
                for d in dominants:
                    b = self.fitness(d)
                    if self.dominates(a, b):
                        rejected.append(d)
                for r in rejected:
                    dominants.remove(r)
        
        return dominants

    def offlineFilter(self, solutions):
        dominants = self.getDominants(solutions)
        
        return dominants