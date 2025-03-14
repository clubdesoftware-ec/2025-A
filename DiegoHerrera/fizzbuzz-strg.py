x = int(input())
s = ""

if x % 3 == 0:
    s += "fizz"
if x % 5 == 0:
    s += "buzz"
if s == "":
    print("no es divisible para 3 ni para 5")

print(s)