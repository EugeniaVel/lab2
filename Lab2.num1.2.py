import numpy as np
A=np.array([7,5])
B=np.array([4,1])
C=np.array([-4,7])
AB=B-A
BC=C-B
CA=A-C
CB=B-C
AC=C-A
BCM=np.linalg.norm(BC)
ABM=np.linalg.norm(AB)
CAM=np.linalg.norm(CA)
OTN=BCM/ABM
BIS=(C+OTN*A)/(1+OTN)
MED=(A+C)/2
cosC=np.dot(CB,CA)/(BCM*CAM)
cosA=np.dot(AC,AB)/(CAM*ABM)
CH=BCM*cosC
AH=ABM*cosA
OT=CH/AH
H=(C+OT*A)/(1+OT)
print("Координаты высоты: " + str(H) + " Координаты биссектрисы: " + str(BIS) + " Координаты медианы: " + str(MED))