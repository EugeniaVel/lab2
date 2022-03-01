import numpy as np
a=np.array([18,-22,-5])
b=np.array([-3,-2,-2])
n=np.cross(a,b)
mn=np.linalg.norm(n)
mm=7
x=mm/mn
m=n*x
print("Координаты вектора m: " + str(m))