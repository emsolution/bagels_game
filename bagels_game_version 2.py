''' this version of bagels game does not repeats digit'''

from random import randint, shuffle
print('''Enter a three digit number.\nThis game is called Bagels. \nYou are to guess a three digit number. \nOnce a digit is correct and in the right position, the computer will display \'Fermi\' \nBut if a digit is correct but not in the right position, the computer will display \'Pico\' \nIf no digit is correct, the computer will display \'Bagels\' ''')
single = False
while single == False:
    num = randint(100,1000)
    num_list = list(str(num))
    if len(set(num_list)) == len(num_list):
        single = True

count, out = 1, False
while out == False:
    check=False
    while check == False:
        try:
            guess = int(input('Enter your guess: '))
            check = True
        except ValueError:
            print('Your guess, is not a number')
            print('Please, enter a valid three digit number')
        else:
            if (len(str(guess)) != 3):
                print(f'Please, {guess} is not a three digit number!')
                print('Enter a three digit number e.g. 234')
        finally:
            pass
            
    guess_list = list(str(guess))
    result = []
    for i, j in enumerate(guess_list):
        if len(guess_list) == len(num_list):
            if  num_list[i] == j:
                result.append('Fermi')
            elif j in num_list:
                result.append('Pico')
    if len(guess_list) == len(num_list):
        if len(result) == 0:
            result.append('Bagels')
        elif result.count('Fermi') == 3:
            result.clear()
        shuffle(result)
        if len(result) != 0: print(' '.join(result))
        
        if guess == num:
            print('Correct')
            out = True
        elif count ==10:
            out = True
        else:
            print(f'you have {10 - count} chances left')
        count += 1
print(num)     