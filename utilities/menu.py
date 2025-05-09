from colorama import Fore, Style
from utilities.converters import UnitConverter
from utilities.validators import InputValidator

def utilities_menu():
    while True:
        print(f"\n{Fore.CYAN}=== UTILITIES ===")
        print("1. Temperature Converter")
        print("2. Email Validator")
        print("3. Number Validator")
        print("4. Back to Main Menu{Style.RESET_ALL}")
        
        choice = input("Select utility: ")
        
        if choice == "1":
            temp = float(input("Temperature: "))
            unit = input("From (C/F): ").upper()
            if unit == "C":
                print(f"{Fore.GREEN}Fahrenheit: {UnitConverter.celsius_to_fahrenheit(temp)}{Style.RESET_ALL}")
            elif unit == "F":
                print(f"{Fore.GREEN}Celsius: {UnitConverter.fahrenheit_to_celsius(temp)}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Invalid unit!{Style.RESET_ALL}")
                
        elif choice == "2":
            email = input("Enter email: ")
            valid = InputValidator.is_valid_email(email)
            print(f"{Fore.GREEN}Email is {'valid' if valid else 'invalid'}{Style.RESET_ALL}")
            
        elif choice == "3":
            num = float(input("Enter number: "))
            valid = InputValidator.is_positive_number(num)
            print(f"{Fore.GREEN}Number is {'positive' if valid else 'not positive'}{Style.RESET_ALL}")
            
        elif choice == "4":
            break
            
        else:
            print(f"{Fore.RED}Invalid choice!{Style.RESET_ALL}")