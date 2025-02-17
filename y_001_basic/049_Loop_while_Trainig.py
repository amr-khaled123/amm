#===========================
#== Loop => While Trainig ==
#===========================

myfavouritewebs = []
maximumwebs = 5

while maximumwebs > 0 :
     web=input("website name without https:// \n")
     myfavouritewebs.append(f"https://{web.strip().lower()}")
     maximumwebs-=1
     print(f"website added : {maximumwebs} places left")
     print(myfavouritewebs)
else:
     print("bookmark is full")
