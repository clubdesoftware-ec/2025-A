def implementacion1(x):
    print("I1")
    if (x % 3) == 0 and (x % 5) == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else: 
        print("no es divisible para 3 ni para 5")

def implementacion2(x):
    print("I2")
    strs = ["fizz", "buzz"]
    vals = [3,5]
    for i in range(len(vals)):
        if x % vals[i] == 0:
            print(strs[i])  


#alcance
if __name__ == "__main__":
    x = int(input())
    implementacion1(x)
    implementacion1(x*3)
    #implementacion2(x) #con esto bloqueo que se corra la segunda