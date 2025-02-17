#===============================================
#===============================================
#== File Handling => Write And Append in File ==
#===============================================
#===============================================

"""mylife=open(r"F:\pythonpych\amr.txt", "w")
mylife.write("hello from 67")
mylife.write("Second Line")
mylife.write("hello from 67")"""

"""mylist=["amr\n","khaled\n","gamal\n"]
mylife=open(r"F:\pythonpych\amory.txt", "w")
mylife.write("Hi\n")
mylife.writelines(mylist)
mylife.write("Hi\n")"""

mylife=open(r"F:\pythonpych\amory.txt", "a")
mylife.write("new sheet")