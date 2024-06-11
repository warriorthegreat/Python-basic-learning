
import os
import shutil
path = r"C:\Users\CKJ\Desktop\workspace"

#刪檔案

# os.remove(f"{path}/test.txt")

#刪空資料夾，如果資料夾裡面有東西會顯示錯誤，防呆。
#os.rmdir(f"{path}/dirc")    


#刪除資料夾以及其內容
#shutil.rmtree()

#把東西丟到資源回收桶
import send2trash

send2trash.send2trash(f"{path}/test.txt")

