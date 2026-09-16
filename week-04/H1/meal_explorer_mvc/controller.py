"""Controller: coordinate the model and view functions.

The controller contains the program flow. Do not create classes.
"""

import model
import view


def show_categories():
    """Fetch and display meal categories."""
    categories = model.get_categories()

    if len(categories) == 0:
        view.display_message("No categories are available right now.")
    else:
        view.display_categories(categories)


def filter_meals_by_category(category):
    """Fetch and display meals for a given category."""
    meals = model.get_meals_by_category(category)

    if len(meals) == 0:
        view.display_message(f"No meals found for category '{category}'.")
    else:
        view.display_meals(meals)


def handle_filter_meals_by_category():
    """Let the user select categories until they enter 0."""
    categories = model.get_categories()

    if len(categories) == 0:
        view.display_message("No categories are available right now.")
        return

    running = True

    while running:
        # Reuse the fetched list instead of calling the API again.
        view.display_categories(categories)
        view.display_message(
            "Enter a category number, or 0 to return to the main menu."
        )

        try:
            choice = int(view.ask_menu_choice())
        except ValueError:
            view.display_message(
                f"Enter a whole number from 1 to {len(categories)}, or 0 to return."
            )
        else:
            match choice:
                case 0:
                    running = False

                case number if 1 <= number <= len(categories):
                    category = categories[number - 1]
                    view.display_message(f"Filtering meals by category: {category}")
                    filter_meals_by_category(category)

                case _:
                    view.display_message(
                        f"Enter a number from 1 to {len(categories)}, or 0 to return."
                    )


def show_random_meal():
    """Ask the model for a random meal and send it to the view."""
    # TODO: Fetch a random meal using the model.
    # Handle an unavailable meal with a message from the view.
    # Otherwise extract its ingredients and display the recipe.
    pass


def search_for_meal():
    """Run the name-search interaction."""
    # TODO: Follow these beginner-sized steps:
    # 1. Get a term by calling view.ask_search_term().
    # 2. If it is empty, display a message and return.
    # 3. Call model.search_meals_by_name(term).
    # 4. If the returned list is empty, display a message and return.
    # 5. Call view.choose_meal(meals).
    # 6. Call model.extract_ingredients(selected_meal).
    # 7. Call view.display_meal(selected_meal, ingredients).
    pass


def show_areas():
    """Coordinate the area-list model and view functions."""
    # TODO: Call model.get_areas().
    # Display a helpful message if the list is empty.
    # Otherwise call view.display_areas(areas).
    pass


def show_ingredients():
    """Coordinate the ingredient-catalog model and view functions."""
    # TODO: Call model.get_ingredients().
    # Display a helpful message if the list is empty.
    # Otherwise call view.display_ingredients(ingredients).
    pass


def search_for_meal_by_area():
    """Search by area, select a result, and load its full recipe."""
    # TODO:
    # 1. Call view.ask_area(); reject empty input.
    # 2. Call model.search_meals_by_area(area); handle an empty list.
    # 3. Call view.choose_meal(meals).
    # 4. Read the selected summary's "idMeal".
    # 5. Call model.lookup_meal_by_id(meal_id); handle None.
    # 6. Extract ingredients and display the full meal.
    pass


def search_for_meal_by_ingredient():
    """Search by one ingredient, select a result, and load its full recipe."""
    # TODO: Follow the area-search steps, but call view.ask_ingredient()
    # and model.search_meals_by_ingredient(ingredient).
    # Look up the selected summary's ID before displaying the recipe.
    pass


def handle_menu_choice(choice):
    """Perform one menu action and return whether to continue."""
    match choice:
        case "1":
            show_categories()

        case "2":
            handle_filter_meals_by_category()

        case "3":
            search_for_meal()

        case "4":
            show_random_meal()

        case "5":
            show_areas()

        case "6":
            show_ingredients()

        case "7":
            search_for_meal_by_area()

        case "8":
            search_for_meal_by_ingredient()

        case "0":
            view.display_message("Goodbye!")
            return False

        case _:
            view.display_message(f"'{choice}' is not a menu option.")

    return True


def run():
    """Repeat the menu until handle_menu_choice returns False."""
    running = True

    while running:
        view.display_menu()
        choice = view.ask_menu_choice()
        running = handle_menu_choice(choice)
