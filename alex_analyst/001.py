import os
import shutil
path = r"A:\ibn_elhaithem"
print(os.listdir(path))
list = [r'\Ibn Al-Haitham.pdf', r'\Ibn Al-Haitham1.pdf',
        r'\Ibn Al-Haitham2.pdf', r'\Ibn Al-Haitham4.pdf', r'\amr.png']
for i in list:
    print(os.path.exists(path+i))

os.makedirs(path+r'\msv')
