from TwoXSAT import TwoXSAT
from tools import parseFile

sat = parseFile('../InstanciasSAT/test.cnf')

twoXSAT = TwoXSAT()
print(twoXSAT.toXSAT(sat,5))