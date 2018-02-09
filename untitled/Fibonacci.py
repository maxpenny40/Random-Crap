total = int(input('Length of Sequence: '))
i= 0
num1 = 0
num2 = 1
final = 0
while i < total:
    final = num1 + num2
    num1 = num2
    num2 = final
    print(final)
    i += 1