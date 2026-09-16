# Instructor Notes

## Why procedural MVC?

This assignment uses MVC as separation of responsibilities, not as an OOP
exercise. Each layer is a module of plain functions. It lets students compare
a one-file imperative script with a multi-file imperative program before they
encounter classes.

The required path stays deliberately small:

1. Model returns lists and dictionaries.
2. View collects input and prints output.
3. Controller uses conditionals and calls the other modules.

Area and ingredient searches now require the filter-to-ID-lookup workflow.
Introduce it after name search: filtering returns summary dictionaries, while
lookup returns the complete recipe. Listing meals by category is now a supplied
controller example; viewing a full recipe from that category list is optional.

## Suggested checkpoints

- Run option 1 and identify the path through all four modules.
- Finish ingredient parsing and the random-meal controller TODO, then test option 4.
- Finish category loading and test option 1.
- Finish category filtering and test option 2, including invalid input and 0.
- Finish search and selection, then test option 3.
- Finish area and ingredient lists, then test options 5 and 6.
- Finish filters and ID lookup, then test options 7 and 8.
- Test invalid text, invalid ranges, no results, and a network failure.

## Manual grading checks

1. `python main.py` starts the menu.
2. Option 1 lists category names.
3. Searching `chicken` displays numbered results.
4. Text and out-of-range input at the result prompt do not crash the program.
5. An unlikely name such as `zzzz-not-a-meal` produces a helpful message.
6. A selected meal displays ingredients and instructions.
7. Option 4 displays a random meal.
8. Option 5 lists area names and option 6 lists ingredient names.
9. Option 7 filters by Canadian and displays a selected full recipe.
10. Option 8 filters by chicken_breast and displays a selected full recipe.
11. Empty area/ingredient input and no-match results are handled safely.
12. An invalid main-menu choice is rejected.
13. Option 0 exits cleanly.
14. Option 2 lists meals by category, rejects invalid input, and returns on 0.
15. The category list is fetched only once per category-selection session.

## Controller example

The supplied code separates `run()` from `handle_menu_choice(choice)`.
Use it to teach Boolean return values: the loop continues on `True` and stops
on `False`. The category-selection loop demonstrates a second, local loop
that stops without exiting the main menu.

## Common beginner mistakes

- Writing API code in `controller.py` instead of calling the model.
- Calling `input` from the model or controller instead of the view.
- Assuming `data["meals"]` is always a list; it can be `None`.
- Forgetting the leading slash in `fetch_json(endpoint)`.
- Treating category meal-name strings as dictionaries. Only the category
  example drops the meal IDs; the other searches preserve dictionaries.
- Passing a second argument to `fetch_json`, which now accepts only an endpoint.
- Confusing the ingredient catalog with a single recipe's numbered ingredients.
- Displaying filter summaries without looking up the full recipe by ID.
- Forgetting that choice 1 corresponds to list index 0.
- Forgetting to increment the ingredient number inside the `while` loop.
- Creating an infinite loop when the ingredient is empty.
- Using a bare `except` instead of catching expected errors.
