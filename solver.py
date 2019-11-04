
class Solver:

    def __init__(self, instances = [], weights = [], solver="random"):
        self.instances = instances
        self.weights = weights
        self.solver = solver
    
    def fitness(self, permutation):
        fitness = 0
        previous = permutation[0]

        for p in permutation:
            for i in range(0,len(self.weights)):
                fitness += self.weights[i] * self.instances[i][previous][p]
            previous = p
        
        return fitness
