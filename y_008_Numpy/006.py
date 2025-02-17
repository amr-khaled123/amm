import numpy as np
a = np.array([1, 2, 4, 5, 3, 0])
# print(a[::-1])
a = np.argsort(a)
print(f"{a}\n{'*'*20}")


n = input().strip().split(' ')
s = int(n[0])*int(n[1])
ls1 = []
for i in range(int(n[0])):
    ls = input().strip().split(' ')
    ls1.append(ls)

a = np.array(ls1, dtype=int)
print(a.T)
print(a.reshape(1, s)[0])
