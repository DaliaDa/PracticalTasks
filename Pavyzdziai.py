#Infinite while loop
while True:
    password = input('Enter your password: ')

    if len(password) < 4:
        print('Password too short')
        continue
    else:
        print(f'You entered {password}')
        break

print(password)

#Nested loop kitas pavyzdys su apibudinimais
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

  # SLICING
        b ="Hello, World!"
print(b[2:5])

b ="Hello, World!"
print(b[:5])

b ="Hello, World!"
print(b[2:])

#printed llo, tada Hello ir galiausiai llo, World


#arguments, returning values
def my_function(number):
    if number > 5:
        return "Value is correct: " + str(number)
    else:
        return "Value is incorrect:" + str(number)
print("===========")
print(my_function(2))