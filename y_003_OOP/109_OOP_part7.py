# ---------------------------------
# -- Object Oriented Programming --
# ---------------------------------


class skill:

    def __init__(self):
        self.skills = ["html", "css", "JS"]
        """
        self.n = int(input("enter number of array: "))
        self.arr = []
        for i in range(0, self.n, 1):
            self.name = input(f"enter you name of row [{i+1}]: ").split()
            self.arr.append(self.name)"""

    def __str__(self):
        return f"names are {self.skills}"

    def __len__(self):
        return len(self.skills)


profile = skill()
print(profile.skills)
print(len(profile.skills))
