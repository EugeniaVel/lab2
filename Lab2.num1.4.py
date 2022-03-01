import math
MM=1
NM=3
cosMN=math.cos(2*math.pi/3)
MN=MM*NM*cosMN
AM=math.sqrt(16*MM**2+8*MN+NM**2) #am=sqrt((4m+n)^2)=sqrt(16m^2+8mn+n^2), тк a=4m+n
BM=math.sqrt(MM**2-6*MN+9*NM**2)  #b=-m+3n
AB=(-4)*MM**2+11*MN+3*NM**2
cosAB=AB/(AM*BM)
pr=2*BM*cosAB
print("Проекция:" + str(pr))