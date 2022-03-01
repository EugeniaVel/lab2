import numpy as np
import math
a=np.array([3,4,5])
b=np.array([1,2,1])
c=np.array([-2,-3,6])
d=np.array([3,-6,3])
#пункт а
ab=b-a
cd=d-c
ad=d-a
abm=np.linalg.norm(ab)
cdm=np.linalg.norm(cd)
adm=np.linalg.norm(ad)
print("Пункт a:")
print("Координаты вектора AB: " + str(ab) + " Модуль вектора AB: " + str(abm))
print("Координаты вектора CD: " + str(cd) + " Модуль вектора CD: " + str(cdm))
print("Координаты вектора AD: " + str(ad) + " Модуль вектора AD: " + str(adm))
#пункт b
ac=c-a
acm=np.linalg.norm(ac)
cosabac=np.dot(ab,ac)/(abm*acm)
angle=np.arccos(cosabac)
print("Пункт b:")
print("Угол между векторами AB и AC: "+str(angle))
#пункт c проекция ad на ab
cosadab=np.dot(ad,ab)/(abm*adm)
padab=adm*cosadab
print("Пункт c:")
print("Проекция вектора AD на AB: " + str(padab))
#пункт d площадь ABD
sinadab=math.sqrt(1-cosadab**2)
Sabd=(abm*adm*sinadab)/2
print("Пункт d:")
print("Площадь ABD: " + str(Sabd))
#пункт e объём пирамиды