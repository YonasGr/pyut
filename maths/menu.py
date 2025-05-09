from colorama import Fore, Style
from maths.operations import MathOperations
from maths.sequences import NumberSequences

def math_menu():
    while True:
        print(f"\n{Fore.CYAN}=== MATH OPERATIONS ===")
        print("1. Basic Arithmetic")
        print("2. Factorial")
        print("3. Prime Check")
        print("4. Fibonacci Sequence")
        print("5. Back to Main Menu{Style.RESET_ALL}")
        
        choice = input("Select operation: ")
        
        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"\n{Fore.GREEN}Addition: {MathOperations.add(a, b)}")
            print(f"Subtraction: {MathOperations.subtract(a, b)}")
            print(f"Multiplication: {MathOperations.multiply(a, b)}")
            print(f"Power: {MathOperations.power(a, b)}{Style.RESET_ALL}")
            
        elif choice == "2":
            n = int(input("Enter number for factorial: "))
            print(f"{Fore.GREEN}Result: {MathOperations.factorial(n)}{Style.RESET_ALL}")
            
        elif choice == "3":
            n = int(input("Enter number to check: "))
            is_prime = MathOperations.is_prime(n)
            print(f"{Fore.GREEN}{n} is {'prime' if is_prime else 'not prime'}{Style.RESET_ALL}")
            
        elif choice == "4":
            n = int(input("Sequence length: "))
            print(f"{Fore.GREEN}Sequence: {NumberSequences.fibonacci(n)}{Style.RESET_ALL}")
            
        elif choice == "5":
            break
            
        else:
            print(f"{Fore.RED}Invalid choice!{Style.RESET_ALL}")