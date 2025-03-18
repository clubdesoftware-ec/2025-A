x = int(input())
#if x % 3 == 0:
#    print("fizz")
#elif x % 5 == 0:
#    print("buzz")
#elif (x % 3) == 0 and (x % 5) == 300:
#    print("fizzbuzz")
#else: 
#    print("no es divisible para 3 ni para 5")

### Corrección
#x = int(input())
#if (x % 3) == 0 and (x % 5) == 0:
 #   print("fizzbuzz")
#elif x % 3 == 0:
#    print("fizz")
#elif x % 5 == 0:
 #   print("buzz")
#else: 
 #   print("no es divisible para 3 ni para 5")
"""
strs = ["fizz", "buzz"]
vals = [3,5]
for i in range(len(vals)):
    if x % vals[i] == 0:
        print(strs[i])    """

d = {
    "fizz": 3, 
    "buzz": 5
}

for i, j in d.items():
    if x % j == 0:
        print(i)

def key():
    for k in d.keys():
        print(k)
        print(d[k])

    for v in d.values():
        print(v)

    for w, k in d.items():
        print(w)
        print(k)