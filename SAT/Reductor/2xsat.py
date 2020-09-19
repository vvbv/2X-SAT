import tools
from SAT import SAT, NextSAT

# Transformación SAT a 3SAT

### Primer condición:
# si K=1, se crean 2 variables nuevas

### Segunda condición:
# si K=2, se crean 1 variable y 2 cláusulas nuevas

### Tercera condición:
# si K=3, se deja como está

### Última condición:
# si K>3, se crean k-3 variables y k-2 cláusulas


def satTo3SAT(SAT:obj)->NextSAT:
    #
    pass

def nextSAT(NextSAT:obj)->NextSAT:
    for clause in NextSAT.clauses:
        pass

def toXSAT(SAT:obj, x):

    if x == 0:
        return obj
    elif true: #SAT
        return toXSAT( satTo3SAT(obj), x-2)
    else if true:
        return toXSAT( nextSAT(obj), x-1)
