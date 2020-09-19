class Clause:

    def __init__():
        pass


class SAT:

    def __init__(self, list:clauses):
        self.clauses = test

    @property
    def clauses(self)->list:
        return self._clauses

    @test.setter
    def clauses(self, list:clauses):
        self._clauses = clauses

    def add_clause():
        pass

class NextSAT(SAT):

    def __init__(self, arg):
        pass


def satTo3SAT(SAT:obj)->NextSAT:
    pass

def nextSAT(NextSAT:obj)->NextSAT:
    for clause in NextSAT.clauses:
        pass

def toXSAT(SAT:obj, x):

    if x == 0:
        return obj

    for i in range(0,x):
        if true: #SAT
            return toXSAT( satTo3SAT(obj), x-1)
        else:
            return toXSAT( nextSAT(obj), x-1)
