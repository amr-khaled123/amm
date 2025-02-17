# --------------------------------------------------
# -- Object Oriented Programming => Encapsulation --
# - Protected
# - Attrbiutes and methods can be accessed from within the class and sub classes mean derived class
# - Attributes and methods prefix with one UnderScore_
# --------------------------------------------------

# Protected
class bombastic:
    def __init__(self, name):
        self._name = name  # protected


class name(bombastic):
    def pri(self):
        print(f"{self._name} from class name")


one = bombastic("Ahmed")
two = name("m")
print(one._name)
print(two.pri())

one._name = "amr"
print(one._name)


# -------------------------
class Member:
    def __init__(self, name):
        self.__name = name  # private

    def returno(self):
        return f"{self.__name} from class Member"


ones = Member("Ahmed")
print(ones.returno())

print(ones._Member__name)  # type: ignore
