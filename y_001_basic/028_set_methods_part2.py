# ---------------
# --set methods--
# ---------------

# difference()
a = {1, 2, 3, 4}
b = {1, 2, 'amr', 4, 'khaled'}
print(a)
print(a.difference(b))  # a fark b = {3}
print(a)  # {1,2,3,4}
print(a-b)  # {3}
print(b.difference(a))  # {'khaled', 'amr'}
print(b)  # {1, 2, 'khaled', 4, 'amr'}
print(b-a)  # {'khaled', 'amr'}
print("="*50)

# dfference_update()
a = {1, 2, 3, 4}
b = {1, 2, 'amr', 4, 'khaled'}
a.difference_update(b)
print(a)  # {3}
print("="*50)


# intersection()
a = {1, 2, 3, 4}
b = {1, 2, 'amr', 'khaled'}
print(a)
print(a.intersection(b))  # (a tkat3 b) = {1,2}
print("="*50)


# intersection_update()
a = {1, 2, 3, 4}
b = {1, 2, 'amr', 'khaled'}
a.intersection_update(b)
print(a)
print("="*50)


# symtric_difference()
i = {1, 2, 3, 4, 5, "x"}
j = {1, 2, "amr", 4, "k"}
print(i.symmetric_difference(j))  # (i ithad j)-( itkat3 j)={3,5,'x','k','amr'}
x = i.union(j)
y = i.intersection(j)
print(x-y)  # ={3,5,'x','k','amr'}
print("="*50)


# symetric_update()
i = {1, 2, 3, 4, 5, "x"}
j = {1, 2, "amr", 4, "k"}
i.symmetric_difference_update(j)
print(i)  # (i ithad j)-( itkat3 j)={3,5,'x','k','amr'}
x = i.union(j)
print(x)  # {1, 2, 3, 4, 5, 'amr', 'k', 'x'}
y = i.intersection(j)
print(y)  # {'k', 'amr'}
print(x-y)
