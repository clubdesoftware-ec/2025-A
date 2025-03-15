print("Hola mundo")


def implementacion1(x):
    if x%3 ==0 and x%5 ==0:
        print("fizzbuzz")
    elif x%5 ==0:
        print("buzz")
    elif x%3 ==0:
        print("fizz")
    else:
        print("no es divisible para 3 ni para 5")

def implementacion2(x):
    strs = ["fizz","buzz"]
    vals = [3,5]
    for i in range(len(vals)):
        if x % vals[i] == 0:
            print(strs[1])


if __name__ == "__main__":
    x = int(input())
    implementacion1(x)
    implementacion2(x*30)
    #implenetación2(x)
    