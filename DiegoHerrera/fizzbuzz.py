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

if residuo == 0:
    print("fizz")
elif divisible5:
    print("buzz")
else:
    print(x)
    # otro codigo
    