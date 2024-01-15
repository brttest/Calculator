def calculator(select, a, b):
    if select == "*":
        return a * b
    elif select == "+":
        return a + b 
    elif select == "-":
        return a - b 
    elif select == "/":
        return a / b


calculator("*", 10, 5)