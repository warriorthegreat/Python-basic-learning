#args arguments 任意數量的參數 會變成tuple  寫成*

#kwargs 關鍵字 + args  = keyword args  變成dictionary  寫成 **

def add(a,b):
    return a + b

print(add(1,2))
#輸出結果 3 
#如果要讓更多數字相加呢? 

#args 
def add1(*args): #代表這個引數可以一直輸入
    total = 0
    for arg in args:
        print(f"arg : {arg}")
        total += arg
    return total           

print(add1(1,2,3,4,5)) 

#輸出結果為5個數字相加成15


#kwargs
def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f'key: {key}, value :{value}')

print_info(name = "alice",age = "25",occupation = "工程師")
#輸出 : 
# key: name, value :alice
# key: age, value :25
# key: occupation, value :工程師