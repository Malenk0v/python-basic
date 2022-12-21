secret_number = 9
guess_count = 1
guess_limit = 3

while guess_count <= guess_limit:
    quess = int(input("Guess: "))
    guess_count += 1
    if quess == secret_number:
        print('You win!')
        break
else:
    print('Sorry, you failed')



