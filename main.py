import argparse
from parser import parseInstance

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('instanceA')
    parser.add_argument('instanceB')

    args = parser.parse_args()

    instanceA = parseInstance(args.instanceA)
    instanceB = parseInstance(args.instanceB)

    print(instanceA)