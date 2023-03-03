while True:
    password = input('Enter your password: ')

    if len(password) < 4:
        print('Password too short')
        continue
    else:
        print(f'You entered {password}')
        break

print(password)