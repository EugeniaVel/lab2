import math
PM=4
QM=2
cosPQ=math.cos(math.pi/6)
PQ=PM*QM*cosPQ
AM=math.sqrt(PM**2-8*PQ+16*QM**2)
BM=math.sqrt(9*PM**2+6*PQ+QM**2)
AB=3*PM**2-11*PQ-4*QM**2
cosAB=AB/(AM*BM)
sinAB=1-cosAB**2
S=AM*BM*sinAB
print("Площадь параллелограмма: " + str(S))