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
    print("Basic Calculator")
    calculator("*", 10, 5)
  