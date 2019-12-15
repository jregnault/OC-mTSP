import numpy as np
import csv

def parseInstance(filename):
    instance = np.empty((100,100), dtype=int)

    with open(filename, 'r') as inputFile:
        for j in range(0,100):
            for i in range(j,100):
                value = int(inputFile.readline())
                instance[i][j] = value
                if i != j:
                    instance[j][i] = value
    
    return instance