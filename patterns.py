
def print_pyramid(rows):
    print("\n--- Pyramid Pattern ---")
    # Outer loop to handle the number of rows
    for i in range(1, rows + 1):
        # Inner loop to print leading spaces for centering
        for j in range(rows - i):
            print(" ", end="")
            
        # Inner loop to print the numbers for the current row
        for k in range(1, i + 1):
            print(k, end=" ")
            
        print()
    print("-" * 25)

def print_right_angled_triangle(rows):
    print("\n--- Right-Angled Triangle Pattern ---")
    # Outer loop to handle the number of rows
    for i in range(1, rows + 1):
        # Inner loop to print numbers.
        for j in range(1, i + 1):
            print(j, end=" ")
        
        print()
    print("-" * 25)

def print_inverted_triangle(rows):
    print("\n--- Inverted Triangle Pattern ---")
    # Outer loop counts down from the total rows to 1
    for i in range(rows, 0, -1):
        # Inner loop prints numbers from 1 up to the current row number 'i'
        for j in range(1, i + 1):
            print(j, end=" ")
            
        print()
    print("-" * 25)

def print_diamond(rows):
    print("\n--- Diamond Pattern ---")
    # Top half of the diamond
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print numbers
        for k in range(1, i + 1):
            print(k, end=" ")
        print()
        
    # Bottom half of the diamond
    for i in range(rows - 1, 0, -1):
        # Print leading spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print numbers
        for k in range(1, i + 1):
            print(k, end=" ")
        print()
    print("-" * 25)
