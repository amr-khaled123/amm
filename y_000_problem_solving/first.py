"""name="osama"
age =18
rank=10
print("my name is {}".format("amr"))#my name is amr
print("my name is {}".format(name))#my name is osama
print("my name is {:.3s} and my age is {:d} and my rank is {:.1f}".format(name,age,rank))#my name is osa and my age is 18 and my rank is 10.0
print("name %.1s"%name)#name o
a,b,c="one","two","three"
print("hello {2} {1} {0}".format(a,b,c))# hello three two one
x,y,z=10,20,30
print("hello {:.2f} {:.2f} {:.2f}".format(x,y,z))#hello 10.00 20.00 30.00
#format in version 3.6++
myname="amr khaled"
age=18
print(f"my name is: {myname} and my age is: {age}")#my name is: amr khaled and my age is: 18
mycomp=5+6j
print("real number {} ".format(mycomp.real))#real number 5.0
print("imagine number {} ".format(mycomp.imag))# imagine number 6.0
print(complex(10.5))#10.5+0j
print(int(10.5))#10
print(float(2))#2.0
x=5
y=x%2
print(y)#1
#print(int(6+10*5/2+4))
print(14%6)#2
#اثنين اس خمسة =(2**5)
print(2**4) #answer=16
print(100//20)#5
print(110//20)#5
print(140//7)#20
print(144//7)#20"""

"""import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 17, 30)
y = np.sin(x)
plt.plot(x, y, marker=".")
plt.show()
data = {"name": ["amr", "khaled", "ahmed"], "faculty": ["computer Science", "medicine", "agriculture"],
        "age": [19, 50, 30]
        }
data_pandas = pd.DataFrame(data)"""

# print(el.Sort(list(range(1000, 0, -1))))

# import elzero as el
# print(el.sortk(list(range(1000, 0, -1))))
# print(el.power(5, 2))
# tree
"""
n = 5
while n != 0:
    n = int(input('enter number'))
    match(n):
        case 2:
            print('i\'m the parent and root')
            n = int(input('enter number'))
            match(n):
                case 5:
                    print('i\'m child of 2')
                    n = int(input('enter number'))
                    match(n):
                        case 9:
                            print('i\'m child of 5')
                            n = int(input('enter number'))
                            match(n):
                                case 4:
                                    print('i\'m child of 9')
                                    break
                                case default:
                                    print('default')
                                    break
                        case default:
                            print('i\'m not child of 5')
                            break
                case 7:
                    print('i\'m child of 2')
                    n = int(input('enter number'))
                    match(n):
                        case 2:
                            print('i\'m child of 7')
                            break
                        case 6:
                            print('i\'m child of 7')
                            n = int(input('enter number'))
                            match(n):
                                case 11:
                                    print('i\'m child of 6')
                                    break
                                case default:
                                    print('i\'m not child off 6')
                                    break
                        case default:
                            print('i\'m not child of 7')
                            break
                case default:
                    print('i\'m not child of 2')
                    break
        case default:
            print('i\'m not in tree')
            break"""
