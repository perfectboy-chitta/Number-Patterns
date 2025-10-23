
def get_positive_integer_input(prompt_message):
    try:
        number = int(input(prompt_message))
        if number <= 0:
            print("Invalid input. Please enter a positive number.")
            return None
        return number
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None
