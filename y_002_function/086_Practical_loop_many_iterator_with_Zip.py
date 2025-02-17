#----------------------------------------------------
#-- Practical => Loop on Many Iterators with Zip() --
#----------------------------------------------------

list1 = [1,2,3,4,5]
list2 = ["A","B","C",'D']
tuble0 = ("man","woman","girl","boy")
dict0 = {'name':'amr', 'age':18, 'coun':'egypt'}

for i,j,k,z in zip(list1,list2,tuble0,dict0):
    print("list 1 item =>",i)
    print("list 2 item =>",j)
    print("tuble 0 item =>",k)
    print('dict item =>',z,'value =>',dict0[z])