class SATvar:

    def __init__(self, name: str, value: bool):
        self.name = name
        self.value = value
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value:str):
        self._name = value

    @property
    def value(self) -> bool:
        return self._value
    
    @value.setter
    def value(self, value: bool):
        self._value = value


class Clause:

    def __init__(self, vars: list):
        self.vars = vars

    @property
    def vars(self) -> list:
        return self._vars

    @vars.setter
    def vars(self, value: list):
        self._vars = value


class SAT:

    def __init__(self, clauses: list):
        self.clauses = clauses if clauses else []

    @property
    def clauses(self) -> list:
        return self._clauses

    @clauses.setter
    def clauses(self, value: list):
        self._clauses = value

    def add_clause(self, clause:list):
        self._clauses.append(clause)


class NextSAT(SAT):

    def __init__(self, clauses: list):
        super(NextSAT, self).__init__(clauses)
