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

function_one()

from math import e 
print(e)

def function_three():
    print(e)
    print(round(e))

function_three()

