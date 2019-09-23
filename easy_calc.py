def is_float(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


i = 0
print("Hi! Welcome to Easy Calculator!")
while i == 0:
    print("Please, enter one of these operations: +, -, *, /, ^ or 'exit' for exit:")
    operation = input()
    if operation == 'exit':
        i = 1
        print("Goodbye!")
        break
    else:
        print("Enter the first number:")
        a = input()
        if is_float(a):
            a = float(a)
        else:
            print("Incorrect number!")
            continue
        print("Enter the second number:")
        b = input()
        if is_float(b):
            b = float(b)
        else:
            print("Incorrect number!")
            continue

    if operation == '/' and b == 0:
        print("Oooops! Divide-by-zero isn't supported by me:( Try other numbers or operation!")
    elif operation == '+':
        print(a+b)
    elif operation == '-':
        print(a-b)
    elif operation == '*':
        print(a*b)
    elif operation == '/':
        print(a/b)
    elif operation == '^':
        print(a**b)
    else:
        print("This operation isn't supported by me:( Try other")
