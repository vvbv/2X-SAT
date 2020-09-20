class SATvar:

    def __init__(self, var_str: str):
        self.value = False if var_str[0] == '-' else True
        self.name = var_str if self.value else var_str.replace('-','')

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

    def __init__(self, literals: list):
        self.literals = literals
        self.var_names = []
        self.vars = []

    @property
    def literals(self) -> list:
        return self._literals

    @literals.setter
    def literals(self, value: list):
        self._literals = list(map(lambda value: SATvar(value),value))
        
    def add_var(self, var_str):
        var = SATvar(var_str)
        if var.name not in self.var_names:
            self.var_names.append(var.name)
            self.vars.append(var)


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

clause = Clause(['-1','2','-5'])