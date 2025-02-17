# --------------------------------------------------
# -- Built in Modules => Insall External Packages --
# --------------------------------------------------
# [1] Moduel Vs Package
# [2] External Package Download From The Internet
# [3] You Can Install package with python package manager PIP
# [4] PIP Install The package and its Dependenceies
# [5] Modules List "https://docs.python.org/3/py-modindex.html
# [6] Package and Modules Directory "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/"
# ---------------------------------------------------------------------

import termcolor
import pyfiglet

print(dir(pyfiglet))
print(pyfiglet.figlet_format("ALAHLY",))
print(termcolor.colored("amr",color="light_yellow"))
print(termcolor.colored(pyfiglet.figlet_format('ALAHLY'), color="green"))
print(termcolor.colored(pyfiglet.figlet_format('Amr'),color='magenta'))
print('*'*40)
print(pyfiglet.COLOR_CODES)
print("hello")