# check number if positive or negative or zero
"""x=0
while x<10:
    n = float(input("enter number\n"))
    if n==0:
        print("it\'s zero number")
    elif n>0:
        print("number is positive")
    else:
        print("number is negative")
    x+=1"""
# number in for is even or odd or zero
# for i in range(11):
#     if i==0:
#         print(f"[{i}] is zero number\n".title())
#     elif i%2==0:
#         print(f"[{i}] is even number\n".title())
#     elif i%2!=0:
#         print(f"[{i}] is odd number\n".title())

# number get from user is negative or positive or zero

"""x=0
while x<=10:
    n = int(input("enter an integer number\n"))
    if int(n) == 0:
        print(f"[{n}] is zero number\n".title())
    elif int(n) % 2 ==0:
        print(f"[{n}] is even number\n".title())
    elif int(n) % 2 !=0 :
        print(f"[{n}] is odd number\n".title())
    x+=1
        """

# Calculate Average Take Number From User
# x=0
# n1=0
# sum=0
# while(x==0):
#     n=float(input("enter number\n"))
#     x=int(input("enter zero to continue\n"))
#     n1+=1
#     sum=float(sum+n)
# average=sum/n1
# print(f"Average = {average}")

#-----------------------------------------------------
"""def get_2d_array_input():

  rows = int(input("Enter the number of rows: "))
  columns = int(input("Enter the number of columns: "))
  array = []
  for row in range(rows):
    input_string = input(f"Enter the elements of row {row + 1} (separated by spaces): ")
    row_list = input_string.split()
    row_list = list(map(int, row_list))
    array.append(row_list)
  return array

array = get_2d_array_input()
print(array)"""

#-----------------------------------------------------
# def x():
#     rows=int(input("enter number\n"))
#     arr=[]
#     for i in range(rows):
#         input_s=input(f"enter elementes of row {i+1} (separeted by spaces): ")
#         y=input_s.split()
#         y=list(map(int,y))
#         arr.append(y)
#     return arr
#
# array = x()
# for i in array:
#     print(i)

def z():
    arr1 = []
    int_2d=input("enter element (separeted by spaces): ")
    y=int_2d.split()
    y=list(map(int,y))
    arr1.append(y)
    return arr1
print(z())

# def find_coordinates(x, y, z, n):
#
#   coordinates = []
#   for i in range(x):
#     for j in range(y):
#       for k in range(z):
#         if i + j + k != n:
#           coordinates.append([i, j, k])
#   return coordinates
#
#
# def main():
#   x, y, z, n = map(int, input().split())
#   coordinates = find_coordinates(x, y, z, n)
#   print(coordinates)
#
#
# if __name__ == "__main__":
#   main()

# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         degree=[[].append]
#         first,second=-100,-100
#         for scores in int(score):
#             if first < scores:
#                 second=first
#                 first=scores
#     print(second)

def x(arr):
    x=min(arr)
    return x
print(x([1,2,5,8,-100]))