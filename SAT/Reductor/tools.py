import os


def readFile(path):
    f = open("../InstanciasSAT/test", "r")
    for line in f:
        if not line.startswith("c"):
            print(line)

def parseFile(path):
    pass
