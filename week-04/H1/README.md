# Recipe App - Imperative Python

## Overview

In this homework, you will build a console application that retrieves recipe
information from [TheMealDB](https://www.themealdb.com/). Users will be able to
list meal categories, areas, and ingredients; list meals by category; search for meals by name, area,
or ingredient; view recipe details; and request a random meal.

This is an **imperative-programming assignment**. You will solve the problem
with variables, Python collections, conditionals, loops, functions, input, and
exception handling.

> **Important:** Do not create classes in this assignment. Do not create
> `Meal`, `Category`, or `Recipe` objects. Information returned by the API will
> remain in Python dictionaries and lists. We will study class-based and OOP
> versions later in the course.

The starter organizes functions into model, view, and controller files. This is
only a way to separate responsibilities; it is not an OOP implementation.

## Learning objectives

After completing this homework, you should be able to:

- declare and use variables with common Python data types;
- explain the difference between module and local scope;
- manipulate strings with methods and f-strings;
- access and process lists, dictionaries, and tuples;
- make decisions with `if`/`elif`/`else`;
- select menu actions with `match`/`case`;
- repeat actions with `while` and `for` loops;
- define functions with parameters and return values;
- accept and validate keyboard input;
- handle expected errors with `try`/`except`/`else`; and
- request and process JSON data from a web API.

## Program organization

The starter contains four Python files:

| File | Responsibility |
| --- | --- |
| `model.py` | Request and process data from TheMealDB |
| `view.py` | Read user input and display information |
| `controller.py` | Control the menu and coordinate model/view functions |
| `main.py` | Start the program |

![Model-View-Controller data flow for the imperative Recipe App](mvc-diagram.png)

The solid arrows show requests or user input moving toward the API. The dashed
arrows show meal data and console output returning to the user. `main.py` only
starts the controller; it does not contain the application logic.

Use functions in every file. Do not add classes or dataclasses.

## Starter code

Download the starter files attached to this Canvas assignment. Keep all files
in the same folder. Last year's GitHub project used classes and is **not** the
starter for this assignment; do not copy its `Meal`, `Category`, or `Recipe`
classes.

You can test the console formatting without making an API request by running
`python view.py`. Its `if __name__ == "__main__":` block displays sample
categories. Run `python main.py` to start the application.

## API information

Review the [TheMealDB API documentation](https://www.themealdb.com/api.php).
The educational test key is `1`, which is already included in the starter's
base URL:

```text
https://www.themealdb.com/api/json/v1/1
```

The required features use these endpoints:

| Purpose | Endpoint | Example |
| --- | --- | --- |
| List categories | `categories.php` | `/categories.php` |
| Search meals by category | `filter.php` | `/filter.php?c=Seafood` |
| Search by meal name | `search.php` | `/search.php?s=chicken` |
| Random meal | `random.php` | `/random.php` |
| List areas | `list.php` | `/list.php?a=list` |
| List ingredients | `list.php` | `/list.php?i=list` |
| Search by area | `filter.php` | `/filter.php?a=Canadian` |
| Search by one ingredient | `filter.php` | `/filter.php?i=chicken_breast` |
| Full recipe by ID | `lookup.php` | `/lookup.php?i=52772` |

The supplied `fetch_json` function demonstrates how to connect to the API:

```python
response = requests.get(
    BASE_URL + endpoint,
    timeout=REQUEST_TIMEOUT,
)
response.raise_for_status()
data = response.json()
```

Do not repeat this code in every feature. Call `fetch_json` from your other
model functions.

An endpoint must start with `/`, for example `"/categories.php"`.
When building an endpoint with user text, use `quote()`, which is already
imported in the model, to encode spaces and punctuation safely.

## Required features

Your completed application must display this menu repeatedly until the user
chooses to exit:

```text
----------------------------------------
MEAL EXPLORER
----------------------------------------
1 - List meal categories
2 - Search meals by category
3 - Search meals by name
4 - Surprise me with a random meal
5 - List meal areas
6 - List meal ingredients
7 - Search meals by area
8 - Search meals by ingredient
0 - Exit
```

### 1. List meal categories

Request all categories from TheMealDB and display each category name on a
separate line with a number starting at 1.

Use:

- a dictionary for the complete JSON response;
- a list for the categories;
- a `for` loop to visit each category; and
- an f-string to display each name.

### 2. Search meals by category

Use the supplied controller example to display numbered categories and ask
the user to choose one. Entering `0` returns to the main menu.

Study the supplied `get_meals_by_category(category)` model example. It calls
`fetch_json(f"/filter.php?c={quote(category)}")` and returns meal-name
strings, or an empty list when unavailable. The controller sends the names
to `view.display_meals(meals)`.

Study the selection loop:

- `try` converts the input to an integer.
- `except ValueError` handles input that is not a whole number.
- `case 0` returns to the main menu.
- `case number if 1 <= number <= len(categories)` validates the selection.
- `case _` handles out-of-range integers.

The controller loads categories once and reuses that list inside the loop.

### 3. Search meals by name

Ask the user to enter all or part of a meal name. Send the text as the `s`
parameter to `search.php`.

If meals are found:

1. Display a numbered list of names.
2. Ask the user to choose a number.
3. Validate the number.
4. Display the selected recipe.

If no meals are found, display a friendly message and return to the main menu.

### 4. Display a recipe

Display the following information when available:

- meal name;
- category;
- area or cuisine;
- ingredients and measurements; and
- cooking instructions.

TheMealDB stores ingredients in numbered dictionary fields:

```text
strIngredient1, strIngredient2, ... strIngredient20
strMeasure1,    strMeasure2,    ... strMeasure20
```

Use a `while` loop and an f-string to construct each dictionary key. Stop when
the ingredient is empty. Store each measurement and ingredient as a tuple in a
list.

### 5. Random meal

Request one meal from `random.php` and display it with the same recipe function
used by the name-search feature.

### 6. List meal areas

Request `/list.php?a=list`. An area is the API's cuisine label,
such as Canadian. Get the list under `"meals"`, collect each `"strArea"`
value, and display the names on separate lines.

Complete `get_areas()` in the model, `display_areas(areas)` in the view,
and `show_areas()` in the controller.

Use `fetch_json("/list.php?a=list")`.

### 7. List meal ingredients

Request `/list.php?i=list`. Get the list under `"meals"`,
collect each `"strIngredient"` value, and display the ingredient names.

Complete `get_ingredients()` in the model, `display_ingredients(ingredients)`
in the view, and `show_ingredients()` in the controller.

Use `fetch_json("/list.php?i=list")`.

This feature lists the API's ingredient catalog. It is different from
`extract_ingredients(meal)`, which reads ingredients from one recipe.

### 8. Search meals by area

Ask the user for an area name from the area list. Reject empty input. Request
`filter.php` with an `a` query parameter and display the matching meals as a numbered
list. If no meals match, display a message and return to the main menu.

Let the user choose a meal. Then request its full recipe using
`lookup.php` with an `i` query parameter before displaying ingredients and instructions.

Calls: `fetch_json(f"/filter.php?a={quote(area)}")`, then
`fetch_json(f"/lookup.php?i={meal_id}")`.

### 9. Search meals by ingredient

Ask for one ingredient. Use `strip()` to remove surrounding whitespace and
`replace(" ", "_")` to replace spaces with underscores in the query.
Request `filter.php` with an `i` query parameter.

Use `fetch_json(f"/filter.php?i={quote(ingredient)}")`.

Display numbered results and allow the user to select one. Look up its full
recipe by ID, just as in the area search. Reject empty input and handle
no-match results without crashing. Search for one ingredient at a time;
multi-ingredient search is not required.

Keep the meal dictionaries in name, area, and ingredient search results.
They contain the details or IDs needed for recipe selection. The simple
category example returns only name strings, so `display_meals()` is for that
example; `choose_meal()` must number the dictionaries' `strMeal` values.

> **Why is another request needed?** Area and ingredient filters return meal
> summaries with `idMeal`, `strMeal`, and `strMealThumb`. They do not return
> cooking instructions or ingredient measurements. Use the selected summary's
> `idMeal` with `lookup_meal_by_id()` to get the complete recipe.

### 10. Menu and program flow

Keep the controller simple:

- `run()` repeats the menu and reads the choice.
- `handle_menu_choice(choice)` contains the main `match` statement.
- Each case calls a separate action function.
- The handler returns `False` to exit or `True` to continue.

Main-menu choices are strings such as `"2"`. Numbered category choices are
integers such as `2`, because that input is converted with `int()`.

Use:

- a `while` loop to repeat the menu;
- `input()` to read the user's choice;
- `match`/`case` to select an action;
- `if` statements to handle missing or empty data; and
- functions to keep each operation separate.

After completing an action, the application should return to the main menu.
Entering `0` should end the loop and display a goodbye message.

## Error handling requirements

Your program must not crash when:

- the user enters text where a number is expected;
- the user enters a number outside the displayed range;
- a search has no matching meals;
- the API is unavailable;
- a request times out; or
- the server returns invalid JSON.

Use `try`/`except`/`else` when converting numbered input and when requesting API
data. Catch expected exceptions rather than using a bare `except`.

## Programming rules

- Do not create classes or dataclasses.
- Do not hard-code meal or category results.
- Do not store complete meal data in global variables.
- Keep the model, view, and controller responsibilities separate.
- Use the supplied function names so the starter modules continue to work
  together.
- Use descriptive `snake_case` names.
- All submitted code must be your own work and you must be able to explain it.

## Testing checklist

Before submitting, confirm that:

- [ ] `python main.py` starts the application.
- [ ] Option 1 displays category names.
- [ ] Option 2 validates a category number and displays its meals.
- [ ] Entering 0 in the category loop returns to the main menu.
- [ ] Searching for `chicken` displays numbered results.
- [ ] A selected recipe displays ingredients and instructions.
- [ ] A search with no matches displays a message instead of crashing.
- [ ] Text entered at a numbered prompt is rejected.
- [ ] A number outside the allowed range is rejected.
- [ ] Option 4 displays a random recipe.
- [ ] Option 5 displays area names.
- [ ] Option 6 displays names from the ingredient catalog.
- [ ] Option 7 searches an area and displays the selected full recipe.
- [ ] Option 8 searches one ingredient and displays the selected full recipe.
- [ ] Area and ingredient searches handle empty input and no matches.
- [ ] An invalid menu choice is rejected.
- [ ] Option 0 exits cleanly.
- [ ] No classes or dataclasses were added.

## Submission

Submit the following to Canvas:

1. All four Python files:
   - `main.py`
   - `model.py`
   - `view.py`
   - `controller.py`

2. Terminal screenshots showing:
   - the main menu and a successful name search;
   - meals listed for a selected category;
   - the area and ingredient lists;
   - a successful area search and its selected recipe; and
   - a successful ingredient search and its selected recipe.

Before submitting, place the files in one folder and run `python main.py` from
that folder to verify that the imports work.

## Grading rubric (100 points)

| Category | Points | Expectations |
| --- | ---: | --- |
| API and model functions | 25 | Lists, category filtering, three search types, and ID lookup |
| View and input validation | 20 | Clear output, numbered choices, and safe input handling |
| Controller and program flow | 20 | Working menu, `match`, loops, and coordinated functions |
| Recipe data processing | 15 | Correct ingredient/measure parsing and formatted details |
| Error handling | 10 | Expected API and input problems do not crash the program |
| Code quality | 10 | No classes, useful names, readable formatting, and correct submission |

## Optional challenges

Complete these only after all required features work:
- Allow users to select a category-filter result and view its full recipe.
- Save favorite meal dictionaries in a list.
- Add colored terminal output or simple ASCII art.

The category filter endpoint returns summary data. To display a full
recipe from one of those results, request `lookup.php?i=MEAL_ID` using the
selected meal's `idMeal`.
For this optional challenge, first change the category model to preserve the
summary dictionaries and update the corresponding view function.
