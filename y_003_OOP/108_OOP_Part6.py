# ---------------------------------
# -- Object Orianted Programming --
# ---------------------------------


class member:
    j = 1
    n = int()

    @staticmethod
    def fact():
        j = 1
        for i in range(1, (member.n)+1, 1):
            member.j *= i
        print(f"factorial of {member.n} = {member.j}")
        member.j = 0

    @staticmethod
    def sum():
        for i in range(1, (member.n)+1):
            member.j += i
        print(f"sum of {member.n} = {member.j}")


y = member
y.n = int(input("enter number to calculate factorial and sum: "))
y.fact()
y.sum()
