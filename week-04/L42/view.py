DIVIDER = "-" * 40

def ask_menu_choice():
    """Ask for and return a menu choice as a stripped string."""
    return input("Choice: ").strip()


def display_menu():
    """Display the main menu."""
    print(DIVIDER)
    print("MEAL EXPLORER")
    print(DIVIDER)
    print("1 - List meal categories")
    print("2 - Search meals by category")
    print("3 - Search meals by name")
    print("4 - Surprise me with a random meal")
    print("0 - Exit")
    print(DIVIDER)


def display_message(message):
    """Display one message followed by a blank line."""
    print(f"{message}\n")

def display_categories(categories):
    """Display a list of meal categories."""
    print(DIVIDER)
    print("Meal Categories:")
    print(DIVIDER)

    for idx,category in enumerate(categories):
        print(f"{idx + 1} - {category}")
    print(DIVIDER)  # Add a blank line after the list

def display_meals(meals):
    """Display a list of meals."""
    print(DIVIDER)
    print("Meals:")
    print(DIVIDER)

    for idx, meal in enumerate(meals):
        print(f"{idx+1} - {meal}")
    print(DIVIDER)  # Add a blank line after the list

if __name__ == "__main__":
    cat = ["Beef", "Chicken"]
    display_categories(cat)