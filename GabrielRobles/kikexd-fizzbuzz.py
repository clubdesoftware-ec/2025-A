x = int(input())

if x%3==0 and x%5==0:
    print ("fizzbuzz") 
elif x%5==0: 
    print("buzz")
elif x % 3 == 0:
    print("fizz")
else: 
    print("no es divisible para 3 ni para 5")