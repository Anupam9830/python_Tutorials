"""
d = {}
t = ()
li = []
print(type(d), type(t), type(li))
"""

d1 = {"harry": "berger", "rohan": "ham", "bill": "cheese", "shiv": {"b": "berger", "l": "ham", "d": "cheese"}}

"""
print(d1["rohan"])
print(d1["shiv"]["b"])
"""

"""
d1["garv"] = {'chicken'}
d1[420] = {"kabab"}
print(d1)
del d1["rohan"]
print(d1)
"""

d2 = {"pot": "clay", "knife": "steel"}

"""
d3 = d2
del d3["pot"]
print(d3)
print(d2)
"""

"""
d3 = d2.copy()
del d3["pot"]
print(d3)
print(d2)
"""

"""
print(d2.get("pot"))
d2.update({"leena": "pepsi"})
print(d2)
"""

print(d2.keys())
print(d2.items())


