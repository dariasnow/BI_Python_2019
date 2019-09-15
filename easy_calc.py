a = float(input())
oper = str(input())
b = float(input())

if oper == '/' and b == 0:
    print("Oooops!")
elif oper in ('+', '-', '/', '*'):
	com = str(a) + oper + str(b)
	print(eval(com))
elif oper == '^':
  print(a**b)
