import requests

BASE_URL = "https://www.themealdb.com/api/json/v1/1"
REQUEST_TIMEOUT = 10  # seconds


def fetch_json(endpoint):
    """Fetch JSON data from the given API endpoint."""
    request_time = 5  # seconds
    try:
        x = requests.get(BASE_URL + endpoint, timeout=REQUEST_TIMEOUT)
        x.raise_for_status()
        data = x.json()  # Parse the JSON response into a Python dictionary
    except requests.HTTPError as e:
        print(f"An error occurred: {e}")
        return None
    except requests.Timeout as e:
        print(f"Request timed out: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    else:
        return data


def get_categories():
    """Fetch and return meal categories from the API."""
    endpoint = "/categories.php"
    data = fetch_json(endpoint)
    categories_names = []

    if data is None:
        return categories_names  # Return an empty list if data is None

    for category in data["categories"]:
        name = category["strCategory"]
        categories_names.append(name)
    return categories_names

def get_meals_by_category(category):
    """Fetch and return meals for a given category from the API."""
    endpoint = f"/filter.php?c={category}"
    data = fetch_json(endpoint)
    meals = []

    if data is None:
        return meals  # Return an empty list if data is None

    for meal in data["meals"]:
        meals.append(meal["strMeal"])
    return meals
