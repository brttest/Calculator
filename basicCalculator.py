def calculator(select, a, b):
    if select == "*":
        return a * b
    elif select == "+":
        return a + b 
    elif select == "-":
        return a - b 
    elif select == "/":
        return a / b

if __name__ == "__main__":
    calculator("*", 10, 5)