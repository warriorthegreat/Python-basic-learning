from tkinter import W


str = r"C:\Users\CKJ\Desktop\workspace\TEST.txt"

text = "hi!\n祝你一切順利!"

#寫入模式:w aka write 雖然說是寫入，但其實是整個覆蓋掉。
with open(str,"w") as file:
    file.write(text)
    
#插入模式:a 不會覆蓋掉前面的檔案。
with open(str, "a")as file:
    file.write("\n gogogo!!!")