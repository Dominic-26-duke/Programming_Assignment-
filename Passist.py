import math

def calculator():
    while True:
        print("Simple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Exit")
        
        choice = input("Choose an operation (1/2/3/4/5/6/7): ")
        
        if choice in ['1', '2', '3', '4']:
            nums = input("Enter numbers separated by space: ")
            nums = [float(num) for num in nums.split()]
            
            if choice == '1':
                print("Result:", add(*nums))
            elif choice == '2':
                print("Result:", subtract(*nums))
            elif choice == '3':
                print("Result:", multiply(*nums))
            elif choice == '4':
                print("Result:", divide(*nums))
        elif choice == '5':
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))
            print("Result:", math.pow(base, exponent))
        elif choice == '6':
            num = float(input("Enter a number: "))
            if num >= 0:
                print("Result:", math.sqrt(num))
            else:
                print("Error: Square root of negative number is not a real number.")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please choose a valid operation.")

if __name__ == "__main__":
    calculator()
