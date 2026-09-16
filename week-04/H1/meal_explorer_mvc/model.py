"""Model: request meal data and convert it into useful Python collections.

Complete the TODOs using functions. Do not create classes.
"""

from urllib.parse import quote

import requests


# These constants are variables in module scope.
BASE_URL = "https://www.themealdb.com/api/json/v1/1"
REQUEST_TIMEOUT = 10


def fetch_json(endpoint):
    """Request one API endpoint and return a dictionary, or return None.

    This function is complete. Use it for every API request.
    """
    try:
        response = requests.get(
            BASE_URL + endpoint,
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
        data = response.json()
    except requests.HTTPError:
        return None
    except requests.Timeout:
        return None
    except requests.RequestException:
        return None
    except ValueError:
        return None
    else:
        return data


def extract_ingredients(meal):
    """Return a list of (measure, ingredient) tuples for one meal."""
    ingredients = []
    number = 1

    # TODO: Follow these steps inside a while loop:
    # 1. Continue while number is less than or equal to 20.
    # 2. Get f"strIngredient{number}" from the meal dictionary.
    # 3. Get f"strMeasure{number}" from the meal dictionary.
    # 4. Use ``or ""`` and .strip() to handle empty values.
    # 5. Break when the ingredient is empty.
    # 6. Append the (measure, ingredient) tuple.
    # 7. Add 1 to number.

    return ingredients


def get_categories():
    """Fetch and return a list of category-name strings."""
    endpoint = "/categories.php"
    data = fetch_json(endpoint)
    category_names = []

    if data is None:
        return category_names

    for category in data["categories"]:
        name = category["strCategory"]
        category_names.append(name)

    return category_names


def get_meals_by_category(category):
    """Fetch and return meal-name strings for one category."""
    endpoint = f"/filter.php?c={quote(category)}"
    data = fetch_json(endpoint)
    meals = []

    if data is None:
        return meals

    if data["meals"] is None:
        return meals

    for meal in data["meals"]:
        meals.append(meal["strMeal"])

    return meals


def search_meals_by_name(search_term):
    """Return meals matching a name, or an empty list."""
    # TODO:
    # 1. Call fetch_json(f"/search.php?s={quote(search_term)}").
    # 2. Return [] if the result is None.
    # 3. The API can return None under "meals" when nothing matches.
    # 4. Return the meal list when matches exist.
    return []


def get_areas():
    """Return a list of area-name strings, or an empty list."""
    # TODO:
    # 1. Call fetch_json("/list.php?a=list").
    # 2. Return [] if the result is None or "meals" is None.
    # 3. Use a for loop to collect each "strArea" value.
    return []


def get_ingredients():
    """Return ingredient-name strings from the API's ingredient catalog."""
    # TODO:
    # 1. Call fetch_json("/list.php?i=list").
    # 2. Return [] if the result is None or "meals" is None.
    # 3. Use a for loop to collect each "strIngredient" value.
    # This catalog is different from extract_ingredients for one recipe.
    return []


def search_meals_by_area(area):
    """Return meal summaries matching one area, or an empty list."""
    # TODO: Call fetch_json(f"/filter.php?a={quote(area)}").
    # Return [] after an error or when "meals" is None.
    # Otherwise return the list under "meals".
    return []


def search_meals_by_ingredient(ingredient):
    """Return meal summaries matching one ingredient, or an empty list."""
    # TODO: Strip the input and replace spaces with underscores.
    # Call fetch_json(f"/filter.php?i={quote(ingredient)}").
    # Return [] after an error or when "meals" is None.
    # Otherwise return the list under "meals".
    return []


def lookup_meal_by_id(meal_id):
    """Return a full meal dictionary, or None when unavailable."""
    # TODO: Call fetch_json(f"/lookup.php?i={meal_id}").
    # Return None after an error or when the meal list is empty.
    # Otherwise return the first dictionary in the "meals" list.
    # Area/ingredient filters do not return full recipe details.
    return None


def get_random_meal():
    """Return one random meal dictionary, or None."""
    # TODO: Request /random.php using fetch_json().
    # Return None if the request fails or no meals are available.
    # Otherwise return the first meal dictionary from the response.
    return None
