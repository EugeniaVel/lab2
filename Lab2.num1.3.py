import numpy as np
M=np.matrix('-2,1,1;3,-2,-3;-1,3,4')
detM=np.linalg.det(M)
if (detM!=0):
    m=np.array(M)
    v=np.array([-4,5,-1])
    r=np.linalg.solve(m,v)
    print("Векторы a,b,c образуют базис.")
    print("Координаты вектора d в данном базисе: " + str(r))
else:
    print("Векторы a,b,c не образуют базис")