# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:33:50 2024

@author: seidih6290
"""

def write_dict(contacts):
    
    with open('contacts2.txt','w') as contact: 
       
        print(f'{"Name":<10}{"Phone":<10}', file=contact)
        print("-"*22, file= contact)
        
        for k, v in contacts.items():
            
            
            print(f'{k:<10}{v:<10}', file=contact)

    
def main():
    
    contacts = {"George":"910-698-7896", "Nina":"910-123-9874","Samantha":"919-985-6325"}
    # write dict content to file
    choice = 0
    write_dict(contacts)
    while choice != 4:
        menu()
        choice = int(input("Enter choice "))
        
        if choice == 1:
            with open("contacts2.txt", "r") as file:
                print(file.read())
        elif choice == 2:
            name = input("Please enter a name to search ")
            with open("contacts2.txt", "r") as file:
                for line in file:
                    if name in line:
                        print(line)
        elif choice == 3:
            phone = input("Please enter a name to search ")
            with open("contacts2.txt", "r") as file:
                for line in file:
                    if phone in line:
                        print(line)
        else:
            print("That is not a valid choice")
            
            
            
    # read file content
    
def menu():
    
    print("\n1 Display File Content")
    print("2) Search by Name")
    print("3) Search by phone")
    print("4)Exit")
    
if __name__ =="__main__":
    
    main()