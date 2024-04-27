#python 中的模組

import math 
# help(math)

#輸出結果
#NAME
# math
# DESCRIPTION
#     This module provides access to the mathematical functions

#裡面有方法可以幫助運算
print(math.pow(2,5))
#輸出結果為2的五次方 32.0

#另一種寫法:
#import math as m 
#用m代替math，之後的寫法都要寫m
#如 print(m.pow(...))

#介紹另外三種方法
#ceil aka 無條件進位 上取整函數（ceiling function )
#floor aka 無條件捨去 下取整函數（英語：floor function
#round 四捨五入

num = 20.6 
print(math.ceil(num))
#輸出進位結果 = 21 
print(math.floor(num))
#輸出結果20
print(round(num))
#結果 = 21 

#單獨引入'子模組'

#寫法 : from math import pi 
#從math 中引入子模組pi 

#自建模組
import my_module as mm 

print(mm.pi)
#變成3.14!
print(mm.area(3))


