def dominates(fitnessA, fitnessB):
    result = True
    for i in range(0,len(fitnessA)):
        result = result and (fitnessA[i] < fitnessB[i])
    return result

def offlineFilter(solver, solutions):
    fitnesses = []
    dominants = []

    for s in solutions:
        fitnesses.append(solver.fitness(s))
    
    for i in range(0, len(fitnesses) - 1):
        isDominated = False
        j = i
        while j != len(fitnesses) and not isDominated:
            if dominates(fitnesses[j],fitnesses[i]):
                isDominated = True
            else:
                fitnesses.remove(fitnesses[j])
        
        if not isDominated:
            dominants.append(solutions[i])
    
    return dominants