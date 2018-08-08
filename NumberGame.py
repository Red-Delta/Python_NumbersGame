import random

Code1 = str(random.randint(0,9))
Code2 = str(random.randint(0,9))
Code3 = str(random.randint(0,9))
Code4 = str(random.randint(0,9))

Tries = 1

print(""" ___  _  ___   _  ___   ___   _ _  ___  ___  ___  ___     
| . \| |/  _> | ||_ _|  /  _> | | || __>/ __>/ __>| . \    
| | || || <_/\| | | |   | <_/\| ' || _> \__ \\\__ \|   / _  
|___/|_|`____/|_| |_|   `____/`___'|___><___/<___/|_\_\<_> 
Welcome to DIGIT GUESSR. You\'re goal is to find a randomly generated 4 digit sequence. To start, guess the first digit, then the second, etc. After 4 digits, the machine will tell you wihich digits are true and false. You have 12 guesses to guess the sequence, and to restart, re-open the code""")

while Tries <= 12:

    Numbers = str(input())
    Number1 = Numbers[0]
    Number2 = Numbers[1]
    Number3 = Numbers[2]
    Number4 = Numbers[3] 
    
    Correct = 0
    displayYesNo = ''

    if Number1 == Code1:
       displayYesNo+='+'
       Correct += 1
    else:
       displayYesNo+='-'

    if Number2 == Code2:
       displayYesNo+='+'
       Correct += 1
    else:
       displayYesNo+='-'

    if Number3 == Code3:
       displayYesNo+='+'
       Correct += 1
    else:
       displayYesNo+='-'

    if Number4 == Code4:
       displayYesNo+='+'
       Correct += 1
    else:
       displayYesNo+='-'

    print(displayYesNo)


    if Correct == 4 and Tries <=12:
       print ("Congratulations, you've won!")
    else:
       pass
    
    Tries += 1

print("game over!")



