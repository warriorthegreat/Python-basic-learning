str = r"C:\Users\CKJ\Desktop\workspace\test.txt"

try:
    with open (str) as file:
        print(file.read())
#避免檔案輸入錯誤無法執行       
except FileNotFoundError:
    print("檔案並不存在")
    
    