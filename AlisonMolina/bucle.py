if False:
    l = [54, 2342, -123, 34]

    for element in range (3,7):
        print (element) 

if False:
    strs = ["fizz", "buzz"]
    vals = [3, 5]
    for i in range(len(vals)):
        print(i)
        if x % vals [i] == 0:
            print(strs[i])

"""d = {
    "fizz" : 3,
    "buzz" : 5
}"""

"""for k in d.keys():
    print(k)
    v = d[k]
    print(v)"""

"""for k, v in d.items():
    print(k)
    print(v)"""

"""for v in d.values():
    print(3)"""


x = int(input())
d = {
    "fizz" : 3,
    "buzz" : 5
}
for key,value in d.items():
    if x % value == 0:
        print(key)