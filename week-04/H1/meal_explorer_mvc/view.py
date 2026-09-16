"""View: get keyboard input and display text in the terminal.

The view does not make API requests. Do not create classes.
"""


DIVIDER = "-" * 40


def display_menu():
    """Display the main menu."""
    print(DIVIDER)
    print("MEAL EXPLORER")
    print(DIVIDER)
    print("1 - List meal categories")
    print("2 - Search meals by category")
    print("3 - Search meals by name")
    print("4 - Surprise me with a random meal")
    print("5 - List meal areas")
    print("6 - List meal ingredients")
    print("7 - Search meals by area")
    print("8 - Search meals by ingredient")
    print("0 - Exit")
    print(DIVIDER)


def ask_menu_choice():
    """Ask for and return a menu choice as a stripped string."""
    return input("Choice: ").strip()


def ask_search_term():
    """Ask for and return a meal name as a stripped string."""
    return input("Enter a meal name: ").strip()


def ask_area():
    """Ask for an area name, such as Canadian."""
    return input("Enter an area from the area list: ").strip()


def ask_ingredient():
    """Ask for one ingredient name."""
    return input("Enter one ingredient: ").strip()


def display_message(message):
    """Display one message followed by a blank line."""
    print(f"{message}\n")


def read_number(prompt, minimum, maximum):
    """Read a whole number within an inclusive range.

    This complete function demonstrates while and try/except/else.
    """
    while True:
        user_text = input(prompt).strip()

        try:
            number = int(user_text)
        except ValueError:
            print("Please enter a whole number.")
        else:
            if minimum <= number <= maximum:
                return number
            print(f"Enter a number from {minimum} through {maximum}.")


def display_categories(categories):
    """Display a list of meal categories."""
    print(DIVIDER)
    print("Meal Categories:")
    print(DIVIDER)

    for idx, category in enumerate(categories):
        print(f"{idx + 1} - {category}")

    print(DIVIDER)
    print()  # Add a blank line after the list.


def display_meals(meals):
    """Display a list of meal-name strings from the category filter."""
    print(DIVIDER)
    print("Meals:")
    print(DIVIDER)

    for idx, meal in enumerate(meals):
        print(f"{idx + 1} - {meal}")

    print(DIVIDER)
    print()  # Add a blank line after the list.


def display_areas(areas):
    """Display each area name on a separate line."""
    # TODO: Follow display_categories using DIVIDER, a heading, and a for loop.
    pass


def display_ingredients(ingredients):
    """Display each ingredient name from the catalog on a separate line."""
    # TODO: Follow display_categories using DIVIDER, a heading, and a for loop.
    pass


def choose_meal(meals):
    """Display numbered meals and return the selected meal dictionary."""
    # TODO:
    # 1. Use enumerate(meals) in a for loop.
    # 2. Print each number and the meal's "strMeal" value.
    # 3. Call read_number to get a choice from 1 through len(meals).
    # 4. Return meals[choice - 1].
    # These are dictionaries, unlike display_meals' category-name strings.
    return None


def display_meal(meal, ingredients):
    """Display the name, category, area, ingredients, and instructions."""
    # TODO: Read the name, category, area, and instructions from meal.
    # Provide helpful defaults for missing or empty values.
    # Use f-strings to display the recipe information.
    # Loop through the (measure, ingredient) tuples to display ingredients.
    # Display a message when the ingredient list is empty.
    # Use DIVIDER to separate the output sections.
    pass


if __name__ == "__main__":
    cat = ["Beef", "Chicken"]
    display_categories(cat)
