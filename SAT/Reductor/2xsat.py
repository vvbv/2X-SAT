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

class TwoXSAT:

    def __init__(self):
        self.iNewSat = 0

    def satTo3SAT(self, obj: SAT)->NextSAT:
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
        return NextSAT(newClauses)

    def nextSAT(self, obj: NextSAT)->NextSAT:

        newClauses = []

        clauses = obj.clauses
        for clause in clauses:

            oldLiterals = []
            for literal in clause.literals:
                oldLiterals.append(literal.getLiteralString())

            newClauses.append(Clause(oldLiterals + ["w" + str(self.iNewSat)]))
            newClauses.append(Clause(oldLiterals + ["-w" + str(self.iNewSat)]))
            self.iNewSat += 1

        return NextSAT(newClauses)

    def toXSAT(self, obj, x):
        if x == 1:
            return obj
        # if x == 2:
        #     return None
        elif obj.isSAT():
            return self.toXSAT(self.satTo3SAT(obj), x - 2)
        elif obj.isXSAT():
            return self.toXSAT(self.nextSAT(obj), x - 1)

#sat = parseFile('../InstanciasSAT/jnh1.cnf')
# sat = SAT(
#     [
#         Clause(['-g','t','s']),
#         Clause(['g','-t','-s'])
#     ]
# )

#print(sat)




sat = parseFile('../InstanciasSAT/jnh1.cnf')
# print(satTo3SAT(sat))
# print(nextSAT(sat))
# sat = SAT(
#     [
#         Clause(['-g','t'])
#     ]
# )
twoXSAT = TwoXSAT()
print(twoXSAT.toXSAT(sat,5))