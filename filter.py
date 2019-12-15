def dominates(fitnessA, fitnessB):
    for i in range(0,len(fitnessA)):
        if fitnessA[i] > fitnessB[i]:
            return False
    return True

def isDominant(solution, solutions):
    if solutions == []:
        return True
    elif dominates(solution, solutions[0]):
        return isDominant(solution, solutions[1:])
    else:
        return False

def offlineFilter(solver, solutions):
    fitnesses = []
    dominants = []

    for s in solutions:
        fitnesses.append(solver.fitness(s))
    
    for f in fitnesses:
        if isDominant(f, fitnesses):
            dominants.append(f)

    return dominants

def onlineFilter(solver, solutions):
    fitnesses = []
    dominants = []

    for s in solutions:
        fitnesses.append(solver.fitness(s))
    
    dominants.append(fitnesses[0])
    fitnesses.remove(fitnesses[0])

    for f in fitnesses:
        dominant = False
        for d in dominants:
            if dominates(f, d):
                dominants.remove(d)
                dominant = True
        if dominant:
            dominants.append(f)
    
    return dominants