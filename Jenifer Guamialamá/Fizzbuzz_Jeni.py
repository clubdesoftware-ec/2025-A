x = int(input())

def impementacion(x)
    if x%3==0 and x%5==0:
        print ("fizzbuzz") 
    elif x%5==0: 
        print("buzz")
    elif x % 3 == 0:
        print("fizz")
    else: 
        print("no es divisible para 3 ni para 5")

def implementacion(x):
    strs = ["fizz", "buzz"]
    vals = [3,5]
    for i in range(len(vals)):
        if x % vals[i]==0:
            print(strs[i])

if __name__ == "__main__"


x = int(input())