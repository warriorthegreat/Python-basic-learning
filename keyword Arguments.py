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