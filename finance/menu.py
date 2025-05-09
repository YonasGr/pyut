from colorama import Fore, Style
from finance.calculator import FinancialCalculator

def finance_menu():
    while True:
        print(f"\n{Fore.CYAN}=== FINANCIAL TOOLS ===")
        print("1. Simple Interest")
        print("2. Compound Interest")
        print("3. Profit/Loss")
        print("4. Back to Main Menu{Style.RESET_ALL}")
        
        choice = input("Select tool: ")
        
        if choice == "1":
            p = float(input("Principal: "))
            r = float(input("Rate (%): "))
            t = float(input("Time (years): "))
            interest, total = FinancialCalculator.simple_interest(p, r, t)
            print(f"\n{Fore.GREEN}Interest: {interest}")
            print(f"Total: {total}{Style.RESET_ALL}")
            
        elif choice == "2":
            p = float(input("Principal: "))
            r = float(input("Rate (%): "))
            t = float(input("Time (years): "))
            interest, total = FinancialCalculator.compound_interest(p, r, t)
            print(f"\n{Fore.GREEN}Interest: {interest}")
            print(f"Total: {total}{Style.RESET_ALL}")
            
        elif choice == "3":
            cost = float(input("Cost Price: "))
            sell = float(input("Selling Price: "))
            print(f"{Fore.GREEN}{FinancialCalculator.calculate_profit_loss(cost, sell)}{Style.RESET_ALL}")
            
        elif choice == "4":
            break
            
        else:
            print(f"{Fore.RED}Invalid choice!{Style.RESET_ALL}")