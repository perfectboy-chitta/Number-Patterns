import patterns
import utils

def main():
    while True:
        print("\nWelcome to the Number Patterns Generator!")
        print("Select a pattern to generate:")
        print("1. Pyramid Pattern")
        print("2. Right-Angled Triangle Pattern")
        print("3. Inverted Triangle Pattern")
        print("4. Diamond Pattern")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Thank you for using the generator. Goodbye!")
            break
            
        if choice in ['1', '2', '3', '4']:
            rows = utils.get_positive_integer_input("Enter the number of rows: ")
            if rows is not None:
                if choice == '1':
                    patterns.print_pyramid(rows)
                elif choice == '2':
                    patterns.print_right_angled_triangle(rows)
                elif choice == '3':
                    patterns.print_inverted_triangle(rows)
                elif choice == '4':
                    patterns.print_diamond(rows)
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
