from colorama import Fore, Style
from geometry.calculator import GeometryCalculator
from geometry.shapes import ShapeValidator, ShapeProperties

def geometry_menu():
    while True:
        print(f"\n{Fore.CYAN}=== GEOMETRY CALCULATIONS ===")
        print("1. Rectangle Area/Perimeter")
        print("2. Circle Area/Circumference")
        print("3. Triangle Area")
        print("4. Validate Triangle")
        print("5. Classify Triangle")
        print(f"6. Back to Main Menu{Style.RESET_ALL}")
        
        choice = input("Select operation: ")
        
        try:
            if choice == "1":
                l = float(input("Length: "))
                w = float(input("Width: "))
                if ShapeValidator.is_valid_rectangle(l, w):
                    print(f"\n{Fore.GREEN}Area: {GeometryCalculator.rectangle_area(l, w)}")
                    print(f"Perimeter: {GeometryCalculator.rectangle_perimeter(l, w)}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Invalid rectangle dimensions!{Style.RESET_ALL}")
                    
            elif choice == "2":
                r = float(input("Radius: "))
                if r > 0:
                    print(f"\n{Fore.GREEN}Area: {GeometryCalculator.circle_area(r)}")
                    print(f"Circumference: {GeometryCalculator.circle_circumference(r)}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Radius must be positive!{Style.RESET_ALL}")
                    
            elif choice == "3":
                b = float(input("Base: "))
                h = float(input("Height: "))
                if b > 0 and h > 0:
                    print(f"{Fore.GREEN}Area: {GeometryCalculator.triangle_area(b, h)}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Base and height must be positive!{Style.RESET_ALL}")
                    
            elif choice == "4":
                a = float(input("Side A: "))
                b = float(input("Side B: "))
                c = float(input("Side C: "))
                valid = ShapeValidator.is_valid_triangle(a, b, c)
                print(f"{Fore.GREEN}Triangle is {'valid' if valid else 'invalid'}{Style.RESET_ALL}")
                
            elif choice == "5":
                a = float(input("Side A: "))
                b = float(input("Side B: "))
                c = float(input("Side C: "))
                print(f"{Fore.GREEN}{ShapeProperties.triangle_type(a, b, c)}{Style.RESET_ALL}")
                
            elif choice == "6":
                break
                
            else:
                print(f"{Fore.RED}Invalid choice!{Style.RESET_ALL}")
                
        except ValueError:
            print(f"{Fore.RED}Please enter valid numbers!{Style.RESET_ALL}")