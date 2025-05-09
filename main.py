import sys
from colorama import Fore, Style, init
from geometry.menu import geometry_menu
from finance.menu import finance_menu
from maths.menu import math_menu
from utilities.menu import utilities_menu

init()

def main():
    while True:
        print(f"\n{Fore.BLUE}=== PYTHON UTILITY TOOLKIT ===")
        print(f"{Fore.CYAN}1. Math Operations")
        print("2. Geometry Calculations")
        print("3. Financial Tools")
        print("4. Utilities")
        print(f"5. Exit{Style.RESET_ALL}")
        
        choice = input(f"{Fore.YELLOW}Select category (1-5): {Style.RESET_ALL}")
        
        if choice == "1":
            math_menu()
        elif choice == "2":
            geometry_menu()
        elif choice == "3":
            finance_menu()
        elif choice == "4":
            utilities_menu()
        elif choice == "5":
            print(f"{Fore.GREEN}Exiting...{Style.RESET_ALL}")
            sys.exit()
        else:
            print(f"{Fore.RED}Invalid choice!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()