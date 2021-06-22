# EXERCISE - 2 (FAULTY CALCULATOR)

i1 = int(input("Enter first number : "))
i2 = int(input("Enter second number : "))

print("1 for addition\n", "2 for subtraction\n", "3 for multiplication\n", "4 for division")
t = int(input())

if t == 1:
    if i1 == 56:
        if i2 == 9:
            print("ans is", 77)
        else:
            print("ans is", i1+i2)
elif t == 2:
    print("ans is", i1-i2)
elif t == 3:
    if i1 == 45:
        if i2 == 3:
            print("ans is", 555)
        else:
            print("ans is", i1 * i2)
elif t == 4:
    if i1 == 56:
        if i2 == 6:
            print("ans is", 4)
        else:
            print("ans is", i1 / i2)



