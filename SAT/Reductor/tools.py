import os

def readFile(path: str):
    if not (os.path.isfile(path)):
        raise Exception("File does not exist in relative path: '" + path + '\'')

    satInstance = []
    for line in open(path, "r"):
        if isNotClauseLine(line):
            satInstance.append(getClauseFromLine(line))
    return satInstance

def getClauseFromLine(line: str):
    satClause = line.replace('\n', '').replace(' 0', '').split(' ')
    while("" in satClause):
        satClause.remove("")
    return satClause

def isNotClauseLine(line: str):
    return not line.startswith("c") and not line.startswith("p")

def parseFile(path):
    pass
