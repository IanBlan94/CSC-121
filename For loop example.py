# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# ask user to enter start, and step values
 
start = int(input('Enter a starting number: '))

end = int(input('Enter a ending number: '))

step = int(input('Enter a step number: '))

#define the headeer row

print(f'\n{"Num":<7}{"Sqr":<7}{"Cube"}')

print("-" * 18)

#start the loop

for num in range(start, end, step):
    
    sqr = num ** 2
    print(f'\n{num:<7}{sqr:<7}{num ** 3}')