x = int(input())
# definir string
s = ""
if x % 3 == 0:
    s += "fizz"
if x % 5 == 0:
    s += "buzz"
if s == "":
    s = "no es divisible para 3 ni para 5"

print (s)

#x = 30
# definir string
#s = "fizzbuzz"
#if 30 % 3 == 0:
#    s += "fizz"
#if x % 5 == 0:
#    s += "buzz"
#    s = "fizzbuzz"
#if False:
#    s = "no es divisible para 3 ni para 5"

#print (s)