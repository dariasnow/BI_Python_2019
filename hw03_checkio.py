

def checkio(a):
    x = []
    for i in a:
        if a.count(i) > 1:
            x.append(i)
    return x


data = [int(i) for i in input('Enter integers separated by spaces: ').split()]
print(checkio(data))
