

def checkio(a):
    x = []
    for element in a:
        if a.count(element) > 1:
            x.append(element)
    return x


data = [int(i) for i in input('Enter integers separated by spaces: ').split()]
print(checkio(data))
