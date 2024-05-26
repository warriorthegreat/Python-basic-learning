# python程式筆記

#### 基礎知識篇
##### function函式 （4/6)
```python=
def say_hello()

say_hello()
```
這就是一種函式，要使用它只需要打say_hello()(記得加括號)就可以。
在函式中可以傳遞參數，或者是運算返回值

```python=
def greeting(name):
    print(f"你好{name}")

greeting("阿柴")
```
他就會顯示：你好 阿柴。

運算後返回值會是這樣：
```python=
#傳遞參數


def add( x , y ):
    return x + y

result = add(3,10)

print(result)
#把print寫在裡面或外面都可以，但在裡面用return, 在外面操作後print出來會比較有彈性。

result_1 = add(3,10)+add(5,10)+add(7,10)
print(result_1)
#會等於45 
```

如果我們在裡面就print 不只要處理return會有none的問題，而且在裡面print的話就已經把寫法固定了（還會print很多次）。

##### 預設引數 （4/22)
```python=

#函式的預設引數 (default arguments)
#定義函數時對某一些參數的預設值。
#減少傳入的參數值，讓函數更有彈性。

def greet (name,greeting = "Hello"): #因為python規定，預設引數需要寫在後面。
    print(f"{greeting},{name}")
    

greet("codeshiba")
#傳回:Hello,codeshiba，因為沒有特別限定greeting，使用預設值hello + 傳入的codeshiba

greet("codeshiba","hi")
#傳回hi,codeshiba
#說明預設引數可以被覆蓋，變成hi了。
```
* 預設引數的功用在於在定義函式的時候可以先預設某個值，到時候使用函數就不用輸入太多值，如就算甚麼都不輸入，呼叫後也可以自動打出hello。
* 小技巧:預設引數需要寫在最後面，因為python是這樣規定的XD。
* 小知識:輸入值可以蓋過預設引數，預設引數就比較像是效率考量，讓函式能有一個啥都不做的固定輸出。

##### 關鍵字引數(4/22)
```python=
#Python 的關鍵字參數(Keyword Arguments)

def hello(greeting,title,first_name,last_name):
    print(f"{greeting},{title},{first_name},{last_name}")
 
hello("你好","先生","小杰","李")
#輸出 你好,先生,小杰,李

#關鍵字參數可以讓我們不用按照順序輸入
hello(greeting = "你好",title="先生",last_name ="李",first_name="小杰")
#輸出 你好,先生,小杰,李，順序不同輸出相同。

def get_phone(country_code,area_code,first,last):
    return f"{country_code}-{area_code}-{first}-{last}"

phone_num = get_phone(country_code="886",area_code="02",last="5678",first="1234")
print(phone_num)
#輸出886-02-1234-5678 first last順序不同，輸出仍按照函數內的預設順序。
```
*關鍵字引數的作用是可讓定義的函數在輸入時更加有彈性，不用按照事先定義好的順序輸入，可以透過寫出關鍵字(ex:country_code="886")來定義裡面的預設值。

*以第一段程式來說，即便我把last與first在關鍵字引數的部分順序寫相反，但輸出值還是一樣!

##### 模組(module)(4/27)
1. 模組是甚麼意思呢，當我們在寫程式的時候若新增了一個python檔案，那就是一個模組，例如xxxx.py。這樣的模組可以透過import導入。
2. 這次學了四個東西，第一個是模組的簡寫法，如math 可以改寫成m；第二個是學會使用無條件進入、捨去、四捨五入三種方法；第三個是只引入子模組(或許是為了效率緣故?不用引入一整個模組直覺上更有效率。)
3. 最後一個蠻實用的，自創一個新模組並定義內容，如改動新模組中pi的定義。

```python=
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
#輸出28.26
```
* 新建模組檔案如下，我只有試改變pi的部分。
```python = 
pi = 3.14

#平方
def square(x):
    return x ** 2
#體積
def cube(x):
    return x ** 3

#計算圓面積
def area (radius):
    return pi * radius ** 2

```
##### 作用域 (Function Scope & LEGB Rule)(4/27)
程式碼：
```python=
#變數範圍與作用域
a = 10
def function_one():
    a = 1
    print("a:",a)


    def function_two():
        b = 2
        print("b:",b)
        print("a:",a)
    function_two()
#輸出：a: 1 b: 2 a: 1
function_one()

from math import e 
print(e)

def function_three():
    print(e)
    print(round(e))

function_three()
#輸出：2.718281828459045 2.718281828459045 3
```
1. 這次所學的作用域是指變數的作用範圍，基本上可以分成四個範圍：Local、Enclosing、Global、Built-in進行搜尋。
2. local 是指 def函式內被定義的變數，如果一個變數是nonlocal 則會往外找也就是enclosing，例如說在此程式碼在執行的時候即便function_two內並沒有定義a，但往外找有，所以仍然可輸出。
3. global是全域變數， def函式之外的都可以算。
4. Built-in：顧名思義就是python內建的函式，當python在LEG命名空間找不到變數，就會在Built-in中搜尋。如from math import e就是內建的。
5. 總結一下，python中找變數會從內到外找，從L找到B ，如果都沒有就會是error。

##### 異常處理(5/4)
程式碼:
```python=
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
    

```
* 這次學習的是如何避免python程式因為錯誤而崩潰。
* 首先我們可以在可能出現異常導致崩潰的程式區塊使用try,except,finally三種來測試(或保護)程式。
* 以這次例子中因為分母不能為0，也要求必須為整數，因此分別將兩種狀況寫在except內，若是出現錯誤就會執行except內的內容。
* finally行則是無論如何都會執行的部分!
* 可以記得的小技巧是，這裡可以將兩種狀況中寫入同一個except，當然也可以用else包含其他的異常狀況。

##### 5/26 應用try & except 練習讀取檔案以及寫入文字進入檔案。
```python=
str = r"C:\Users\CKJ\Desktop\workspace\test.txt"

try:
    with open (str) as file:
        print(file.read())
#避免檔案輸入錯誤無法執行       
except FileNotFoundError:
    print("檔案並不存在")
    
text = "hi!\n祝你一切順利!"

#寫入模式:w aka write 雖然說是寫入，但其實是整個覆蓋掉。
with open(str,"w") as file:
    file.write(text)
    
#插入模式:a 不會覆蓋掉前面的檔案。
with open(str, "a")as file:
    file.write("\n gogogo!!!")
```

* 這次的練習先學習了如何讀取python檔案，在讀取檔案的時候會複製文件的路徑，使用r"..."的寫法就可以不用更改路徑的斜線(\)。
* 之後為了避免輸入的路徑錯誤而程式當掉，因此加上try &except 的異常處理使程式可以在錯誤的情況下輸出:「檔案並不存在」
* 接著學習w (寫入)& a(插入)兩種模式，前者是直接以新內容覆蓋舊內容，後者則是在文件後面插入新的文字。
* w & a的寫法很簡單，只是把file.read 改成 file.write，以及在str後面加入w 或 a就可以了!
####  實作篇
##### 4/22 剪刀石頭布
程式碼:
```python=
#這是剪刀石頭布的遊戲

from optparse import Option
import random

player = None #放玩家出的拳種
computer = None #放電腦出的拳種
option = ("剪刀","石頭","布")                                       # tuple 運行速度快也不用修改。
running = True                                                      #確保連續運行

while running:# 其實就是TRUE 一直運行
    player = input("請輸入剪刀、石頭、布:")
    while player not in option :                                    #如果沒有出三種之一的拳種:
        player = input("輸入錯誤:請輸入剪刀、石頭、布:")            #請玩家重新打一次，避免玩家亂打。
    computer = random.choice(option)                        #從option內隨機選出一種拳。
    print(f"玩家出:{player}，電腦出:{computer}")
    
    
    if  player == computer:                     #接下來是遊戲規則，列出玩家獲勝的部分。
        print("平手")
    elif player == "剪刀" and computer == "布":
        print("玩家獲勝")
    
    elif player == "石頭" and computer == "剪刀":
        print("玩家獲勝")
    
    elif player == "布" and computer == "石頭":
        print("玩家獲勝")
    else:                                       #其他狀況電腦獲勝
        print("電腦獲勝")
    
    play_again = input("你要再玩一次嗎?(y/n)?").lower()  #結束遊戲的條件
    if  play_again == "n":
        break

print("謝謝，遊戲結束")

```
在這個程式中，首先我們可以分成四個部分來寫:
*第一部分:
    option : 是放三種拳種(使用tuple，運行速度比list快，也不用修改內容)
    player&computer:拿來放置拳種，一開始為none。
    running:確保可以重複運行的關鍵，為true。
    
*第二部分:
寫player輸入的拳種，以及考慮如果player亂打的處理(通常是再打一次)
寫com用random.choice從option中選擇任一拳種。
顯示各自的拳種讓玩家知道。

*第三部分:
判斷玩家與電腦誰贏的規則，這邊只要列出玩家贏的可能就好(畢竟條件不多)，
其他的可能就是電腦贏，用else概括，相對簡單。

*第四部份:
問玩家是不是要再玩一次也相對簡單，用break就可以結束while迴圈，並在最後感謝玩家遊戲結束。

##### 用Python檢測檔案是否存在(環境為Windows)(5/11)
1. 使用內建的os模組來實作，環境為Windows作業系統。
2. 創建一個資料夾並新增文字文件(txt檔案)，複製路徑，注意在編譯器裡面要把路徑的斜線顯示出來的話，得在字串前面加上r，或者是每個斜線再多一個斜線才能正常顯示。ex : / => // 。這裡採用前面加r的寫法，比較簡單。
3. os模組中有幾個判別此路徑是甚麼東西的方法:
    * exists(...)為判斷此路徑是否存在
    * isfile(...)判斷此路徑是檔案
    * isdir(...) 判斷此路徑是目錄
    * 最後當然可以寫else歸類出其他。
* 覺得這次練習沒啥用，在一般使用上不如直接點過去就知道是連結到甚麼了@@。

```python=
import os

str = r"C:\Users\CKJ\Desktop\workspace"

print(str)

if os.path.isfile(str):
    print("該路徑是檔案")
elif os.path.isdir(str):
    print("該路徑是目錄")
else:
    print("其他")
```