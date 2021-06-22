"""
s = set()
print(type(s))
"""

# s = set([1, 2, 3, 4, 5, 6])
# print(s)

li = [1, 2, 3, 4, 5, 6]
s = set(li)
# print(s)

"""
s.add(1)
print(s)
s.add(1)
print(s)    # set prints unique value

s.add(78)
print(s)
s.add(78)
print(s)
"""


"""
s1 = s.union([9, 8, 7, 6])
print(s, s1)
s3 = s.intersection([5, 6, 7])
print(s, s3)

print(len(s3))
print(max(s))
print(min(s3))

s2 = ([2, 9])
print(s.isdisjoint(s2))
"""