while True:
    password = input('Enter your password: ')

    if len(password) < 4:
        print('Password too short')
        continue
    else:
        print(f'You entered {password}')
        break

print(password)

#kitas pavyzdys su apibudinimais
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)