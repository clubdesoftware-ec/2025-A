x = 30
strs = ["fizz", "buzz"]
vals = [3, 5]

for  i in range(len(vals)):
    if x % vals[i] == 0:
        print(strs[i])

