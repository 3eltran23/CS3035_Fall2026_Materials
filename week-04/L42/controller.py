import view
import model 

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
  
    categories = model.get_categories()
    running = True if len(categories) > 0 else False

    while running:
        show_categories()
        view.display_message("Enter the number of the category to filter meals, or 0 to return to the main menu.")
        try:
            choice = int(view.ask_menu_choice())
        except ValueError:
            view.display_message(f"Invalid input. Please enter a number between 1-{len(categories)}.")
        else:
            match choice:
                case 0:
                    running = False
                case number if 1 <= number <= len(categories):
                        category = categories[choice - 1]
                        view.display_message(f"Filtering meals by category: {category}")
                        filter_meals_by_category(category)
                case _:
                        view.display_message(f"Invalid choice. Please enter a number between 1-{len(categories)}.")
            

def handle_menu_choice(choice):
    match choice:
        case "1":
            pass

        case "2":
            pass

        case "3":
            pass

        case "4":
            pass

        case "0":
            view.display_message("Goodbye!")
            return False

        case _:
            view.display_message(f"'{choice}' is not a menu option.")

    return True

def run():
    running = True
    while running:
        view.display_menu()
        choice = view.ask_menu_choice()
        running = handle_menu_choice(choice)
if __name__ == "__main__":
    print("Controller")
    run()