# ---------------------------------------------
# -- Object Oriented Programmming =>Abstract --
# ---------------------------------------------


from abc import ABCMeta, abstractmethod


class programming(metaclass=ABCMeta):

    @abstractmethod
    def has_oop(self):
        'yes'

    @abstractmethod
    def has_not_oop(self):
        return 'no'


class python(programming):

    def has_oop(self):
        return 'Yes'


class html(programming):

    def has_oop(self):
        return 'No'

    def has_not_oop(self):
        return super().has_not_oop()


one = html()
# two = html()
print(one.has_not_oop())
# print(two.has_not_oop())
