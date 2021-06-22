# EXERCISE - 1

"""
d1 = {"brain": "hair", "hand": "finger", "body": "neck", "leg": "toe"}

print("enter the word :")
i = input()
w = d1[i]
print("the meaning of the word is", w)
"""

"""
d1 = {"brain": "hair", "hand": "finger", "body": "neck", "leg": "toe"}

i = input("enter the word :")
print("the meaning of the word is", d1[i])
"""

d1 = {"brain": "hair", "hand": "finger", "body": "chest", "leg": "toe"}

i = input("enter the word :")
print("the word emphasizes", d1.get(i))
