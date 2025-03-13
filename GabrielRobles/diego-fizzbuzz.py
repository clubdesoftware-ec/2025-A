x = int(input())

d = {
    "fizz" : 3,
    "buzz" : 5
}

for key, value in d.items():
    if x % value == 0:
        print(key)
