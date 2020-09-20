from SAT import SAT, NextSAT, Clause
from tools import parseFile

# Transformación SAT a 3SAT

### Primer condición:
# si K=1, se crean 2 variables y 4 clausulas

### Segunda condición:
# si K=2, se crean 1 variable y 2 cláusulas nuevas

### Tercera condición:
# si K=3, se deja como está

### Última condición:
# si K>3, se crean k-3 variables y k-2 cláusulas


def satTo3SAT(obj: SAT)->NextSAT:
    newClauses = []
    i = 0
    clauses = obj.clauses
    for clause in clauses:
        k = clause.literals.__len__()
        if(k==1):
            varN1 = "v" + str(i)
            varN2 = "v" + str(i+1)
            c1 = Clause([varN1,varN2,clause.literals[0].getLiteralString()])
            c2 = Clause(["-" + varN1,varN2,clause.literals[0].getLiteralString()])
            c3 = Clause([varN1,"-" +varN2,clause.literals[0].getLiteralString()])
            c4 = Clause(["-" +varN1,"-" +varN2,clause.literals[0].getLiteralString()])
            newClauses.append(c1)
            newClauses.append(c2)
            newClauses.append(c3)
            newClauses.append(c4)
            i += 2
        elif(k==2):

            varN1 = "v" + str(i)
            c1 = Clause([varN1,clause.literals[0].getLiteralString(), clause.literals[1].getLiteralString()])
            c2 = Clause(["-" + varN1, clause.literals[0].getLiteralString(), clause.literals[1].getLiteralString()])
            newClauses.append(c1)
            newClauses.append(c2)
            i += 1
        elif (k == 3):
            newClauses.append(clause)
        elif (k >= 4):
            varN = []
            for f in range(0, k-3):
                varN.append("v" + str(i))
                i += 1

            for otroF in range(0, (k-2)):
                if(otroF == 0):
                    newClauses.append(Clause([clause.literals[0].getLiteralString(), clause.literals[1].getLiteralString(), varN[0]]))
                elif(otroF == (k-3)):
                    newClauses.append(Clause([str("-") + varN[-1], clause.literals[-2].getLiteralString(), clause.literals[-1].getLiteralString()]))
                else:
                    newClauses.append(Clause([str("-") + varN[otroF-1], clause.literals[otroF+1].getLiteralString(), varN[otroF]]))
    return SAT(newClauses)



#sat = parseFile('../InstanciasSAT/jnh1.cnf')
# sat = SAT(
#     [
#         # Clause(
#         #     ['-a', 'c']
#         # ),
#         # Clause(
#         #     ['-q']
#         # ),
#         # Clause(
#         #     ['-q','a']
#         # ),
#         # Clause(
#         #     ['-g','t','s']
#         # ),
#         Clause(
#             ['-g','t','s','m', "w", "A", "B", "F"]
#         )
#     ]
# )

#print(sat)

sat = parseFile('../InstanciasSAT/jnh1.cnf')
print(satTo3SAT(sat))











def nextSAT(obj: NextSAT)->NextSAT:
    for clause in NextSAT.clauses:
        pass

def toXSAT(obj: SAT, x):

    if x == 0:
        return obj
    elif True: #SAT
        return toXSAT( satTo3SAT(obj), x-2)
    elif True:
        return toXSAT( nextSAT(obj), x-1)


