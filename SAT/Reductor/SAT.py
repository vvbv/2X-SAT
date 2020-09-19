class SATvar:

    def __init__(self, name):
        self.name = name

    @property
    def name()->str:
        return self._name

    @name.setter
    def name(str:name):
        self._name = name

    @property
    def value():
        return self._value


class Clause:

    def __init__(self, list:vars):
        self.vars = vars

    @property
    def vars()->list:
        return _vars

    @vars.setter
    def vars(list:vars):
        self._vars = vars


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
