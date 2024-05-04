# 異常處理，容許例外避免程式崩潰

#exception 

try:
    x = int(input("請輸入一個整數:"))
    y = int(input("請輸入另一個整數:"))
    print(x / y) #y = 0 則會發生錯誤

except ZeroDivisionError:
    print("除數不能為0")
    # 輸出
    # 請輸入一個整數:10
    # 請輸入另一個整數:0
    # 除數不能為0 沒有直接程式崩潰

except ValueError:
    print("除數必須為整數")
    
# else:
#     print("其他錯誤會跑來這邊")

# except(ZeroDivisionError,ValueError):
#     print("請重新輸入:")
    
finally:
    print("這作用是無論是否出現異常都會執行")
    
