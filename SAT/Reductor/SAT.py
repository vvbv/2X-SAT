class SATvar:

    def __init__(self, var_str: str):
        self.name = var_str.replace('-','') if '-' in var_str else var_str

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value:str):
        self._name = value


class SATLiteral(SATvar):

    def __init__(self, var_str: str):
        super(SATLiteral, self).__init__(var_str)
        self.value = False if '-' in var_str else True

    @property
    def value(self) -> bool:
        return self._value

    @value.setter
    def value(self, value: bool):
        self._value = value


class Clause:

    def __init__(self, literals: list):
        self.vars = []
        self.var_names = []
        self.literals = literals

    @property
    def literals(self) -> list:
        return self._literals

    @literals.setter
    def literals(self, literals: list):
        self._literals = []
        for literal in literals:
            self._literals.append(SATLiteral(literal))
            self.add_var(literal)
        
    def add_var(self, var_str):
        var = SATvar(var_str)
        if var.name not in self.var_names:
            self.var_names.append(var.name)
            self.vars.append(var)

    def __str__(self):
        to_return = "("
        for literal in self.literals:
            to_return = to_return + ("-" if not literal.value else "") + str(literal.name) + " ∨ "
        return to_return[:-3] + ")"

class SAT:

    def __init__(self, clauses: list):
        self.vars = []
        self.clauses = clauses if clauses else []

    @property
    def clauses(self) -> list:
        return self._clauses

    @clauses.setter
    def clauses(self, clauses: list):
        self._clauses = []
        for clause in clauses:
            self.add_clause(clause)

    def add_clause(self, clause):
        clause_vars = clause.vars
        for clause_var in clause_vars:
            add = True
            for var in self.vars:
                if clause_var.name == var.name:
                    add = False
                    break
            if add:
                self.vars.append(clause_var)
        self._clauses.append(clause)

    def __str__(self):
        to_return = ""
        for clause in self._clauses:
            to_return = to_return + str(clause) + " ^ "
        return to_return[:-3]


class NextSAT(SAT):

    def __init__(self, clauses: list):
        super(NextSAT, self).__init__(clauses)


