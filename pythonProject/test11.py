i = 0

"""
while i < 79:
    print(i)
    i = i + 1
"""

"""
while i < 79:
    print(i, end=" ")
    i = i + 1
    """

"""
while True:
    print(i)
    i = i + 1   # infinity loop
"""

"""
while True:
    print(i)
    i = i + 1
    if i > 76:
        break
"""

"""
while True:
    if i < 9:
        continue
    print(i)
    if i == 39:
        break
    i = i + 1
"""


while True:
    k = int(input("enter a num: "))
    if k < 100:
        print("congrats, try again!")
        continue
    else:
        break
