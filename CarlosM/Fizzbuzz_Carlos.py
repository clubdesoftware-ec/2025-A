x = int(input())

### imprime fizz, divisible para 3
### imprime buzz, divisible para 5
### imprime fizzbuzz, divisible para los dos
### Si no es divisible ni para 3 ni para 5, imprime el numero
residuo3 = x % 3

divisible5 = (x % 5) == 0

# Entrada:
# residuo es numero
# 0 es numero
# Salida:
# T/F booleano

if residuo3 == 0:
    print("fizz")
elif divisible5:
    print("buzz")
else:
    print(x)
    #otrocodigo