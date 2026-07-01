def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "0で割ることはできません"
    return a / b

if __name__=="__main__":
    print("計算機アプリ")
    print(add(5,3))
    print(subtract(10,4))
    print(multiply(6,7))
    print(divide(20,4))