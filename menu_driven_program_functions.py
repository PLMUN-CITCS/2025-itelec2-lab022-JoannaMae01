"""
Simple Menu-Driven Program

This program presents a menu to the user, allowing them to:
1. Receive a greeting message.
2. Check if a number is even or odd.
3. Exit the program.

Features:
- Menu-driven structure with a continuous loop
- Function decomposition for modularity
- Input validation for menu selection and number entry
"""

def display_menu() -> None:
    """
    Displays the program's menu options to the user.
    """
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")


def greet_user() -> None:
    """
    Prints a simple greeting message.
    """
    print("Hello! Welcome!")


def get_integer_input(prompt: str) -> int:
    """
    Prompts the user for an integer input and validates it.

    Args:
        prompt (str): The message displayed to the user when asking for input.

    Returns:
        int: A valid integer entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer.")


def check_even_odd(number: int) -> str:
    """
    Determines if a given number is even or odd.

    Args:
        number (int): The integer to check.

    Returns:
        str: A message indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    return f"{number} is an Odd number."


def even_odd_checker_action() -> None:
    """
    Handles the process of getting a number input and checking if it's even or odd.
    """
    number = get_integer_input("Enter an integer: ")
    print(check_even_odd(number))


def handle_menu_choice(choice: int) -> bool:
    """
    Executes the corresponding action based on the user's menu choice.

    Args:
        choice (int): The menu option chosen by the user.

    Returns:
        bool: True if the program should exit, False otherwise.
    """
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True  # Signal to exit the loop
    else:
        print("Error: Invalid choice. Please enter a number between 1 and 3.")
    return False  # Continue the loop


def main():
    """
    Main function that continuously displays the menu and handles user choices.
    """
    while True:
        display_menu()
        choice = get_integer_input("Enter your choice (1-3): ")
        if handle_menu_choice(choice):
            break  # Exit the loop when the user selects option 3


if __name__ == "__main__":
    main()
