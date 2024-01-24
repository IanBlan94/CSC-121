# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 13:32:40 2024

@author: blanchai4714
"""

emp_num = int(input("Enter number of employees: "))

# Define and assign initial value before the loop
# Create a running total

total = 0
for num in range(1, emp_num+1):

    # Calculate gross pay
    print("\nInfo for Employee #", num)
    hours = float(input(" Enter the hours worked: "))
    
    rate = float(input(" Enter the pay rate: "))
    
    gross = hours * rate
    total += gross
    print(f'Gross Pay ${gross}')
    print(f'\nTotal salaries ${total}')