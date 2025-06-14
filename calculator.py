# basic calculator project in python 

def add(a,b):
    return a+b       #function for performing addition

def sub(a,b):          
    return a-b       #function for performing subtraction

def mul(a,b):
    return a*b       #function for performing multiplication

def div(a,b):
    if b!= 0:
      return a/b        #function for performing division
    else:
        return "Error: Division by zero is not allowed."  #handling division by zero

print("Welcome to the  Python Calculator")


while True:
    try:

        a= int(input("Enter first number: "))  #taking input from user
        b = int(input("Enter second number: "))  #taking input from user
        
        
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice == '1':
            print(f"{a} + {b} = {add(a,b)}")
        elif choice == '2':
           print(f"{a} - {b} = {sub(a,b)}")
        elif choice == '3':
            print(f"{a} * {b} = {mul(a,b)}")
        elif choice == '4':
                print(f"{a} / {b} = {div(a,b)}")
        
        
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break  
        else:
            print("Invalid input. Please select a valid operation (1/2/3/4/5).")  
    except ValueError:
            print("Invalid input. Please enter a valid number.")
        
