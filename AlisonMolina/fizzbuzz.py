###residuo3 = x % 3
###divisible5 = x % 5 == 0
#Entrada:
#residuo es numero
#0 es numero
#salida:
# T/F booleano
###print(residuo3 == 0)
"""
if x % 5 == 0 and x % 3 ==0:
        print("fizzbuzz")

elif x % 5 == 0:
        print("buzz")

elif x % 3 == 0:
        print("fizz")

else:
        print("no es divisible para 3 ni para 5")"
        """
"""
x = int(input())
s = ""
if x % 3 == 0:
    s = s + "fizz"
print(s) """""
if False:
    x = int(input())
    for i in [3,5]:
        if x % i == 0:
            print ("here")

x = int(input())
strs = ["fizz", "buzz"]
vals = [3, 5]
for i in range(len(vals)):
    if x % vals [i] == 0:
        print(strs[i])