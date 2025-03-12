#check number
def numbers():
    numbers = int(input("Enter any number:"))
    if numbers % 2 == 0:
        print(numbers, "is an Even number.")
    else:
        print(numbers, "is an Odd number.")   
        
numbers()

while True:
    a = input("Run again?:") 
    if a == "Yes":
        numbers()
        
    else:
        b = print("Program Done")
        break