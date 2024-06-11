import shutil
from tkinter import W

#三種方法

w = r'C:\Users\CKJ\Desktop\workspace'
source = f"{w}/source_file.txt"
dst =  f"{w}/destination_file.txt"
shutil.copyfile(source, dst)
