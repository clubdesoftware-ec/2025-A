x = int(input())

### imprimir fizz, divisible para 3
### imprimir fizz, divisible para 5
### imprimir fizzbuzz, divisible para los dos
### Si no es divisible ni para 3 ni para 5, imprimir el numero

residuo = x % 3

divisible5 = (x % 5) == 0
print(divisible5)
# Entrada
# residuo es numero
# 0 es número
# Salida:
# T/F booleano

#if residuo == 0:
 #   pass
  #  pass
   # pass
#else: 
 #   pass
  #  pass
   # pass


x= int(input())
f="fizz"
b="buzz"
fb= f+b
s= " "
if x % 3 ==0:
    s=s + "fizz"
for i in [3, 5]:
    if x % i ==0:
        print("here")


def implementacion1 (x):
    strs = ["fizz", "buzz"]
    vals = [3, 5]
    for i in range(len(vals)):
        if x % vals[i]==0:
            print(strs[i])

x = int(input())