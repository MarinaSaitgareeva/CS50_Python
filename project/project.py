import requests
import random


def main():
    while True:
        diet = get_diet()
        meal_type = get_meal_type()
        ingredients = get_ingredients()
        max_ready_time = get_max_ready_time()

        try:
            recipies = get_recipes(diet, meal_type, ingredients, max_ready_time, 100)
            recipe = get_random_recipe(recipies)
            return print(recipe)

        except Exception:
            continue


def get_diet():
    while True:
        available_diets = ["None", "Gluten Free", "Ketogenic", "Vegetarian", "Lacto-Vegetarian", "Ovo-Vegetarian", "Vegan", "Pescetarian", "Paleo", "Primal", "Low FODMAP", "Whole30"]

        selected_diet = input("\n Select diet type: \n 1. None \n 2. Gluten Free\n 3. Ketogenic \n 4. Vegetarian \n 5. Lacto-Vegetarian \n 6. Ovo-Vegetarian \n 7. Vegan \n 8. Pescetarian \n 9. Paleo \n 10. Primal \n 11. Low FODMAP \n 12. Whole30 \n Your diet type: ").strip()

        try:
            if not selected_diet:
                return ""
            elif 0 < int(selected_diet) < 13:
                return available_diets[int(selected_diet) - 1]

        except Exception:
            continue


def get_meal_type():
    while True:
        available_meal_type = ["none", "main course", "side dish", "dessert", "appetizer", "salad", "bread", "breakfast", "soup", "beverage", "sauce", "marinade", "fingerfood", "snack", "drink"]
        selected_meal_type = input("\n Select meal type: \n 1. None \n 2. Main course \n 3. Side dish \n 4. Dessert \n 5. Appetizer \n 6. Salad \n 7. Bread \n 8. Breakfast \n 9. Soup \n 10. Beverage \n 11. Sauce \n 12. Marinade \n 13. Fingerfood \n 14. Snack \n 15. Drink \n Your meal type: ").strip()

        try:
            if not selected_meal_type:
                return ""
            elif 0 < int(selected_meal_type) < 15:
                return available_meal_type[int(selected_meal_type) - 1]

        except Exception:
            continue


def get_ingredients():
    while True:
        ingredients = input("\n A comma-separated list of ingredients that the recipes should contain: ").strip()

        if (not ingredients) or ingredients.isnumeric():
            continue
        return ingredients.lower()


def get_max_ready_time():
    while True:
        max_ready_time = input("\n The maximum time in minutes it should take to prepare and cook the recipe: ").strip()

        try:
            return int(max_ready_time)

        except Exception:
            continue


def get_recipes(diet, meal_type, ingredients, max_ready_time, number):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"

    # ranking - Whether to maximize used ingredients (1) or minimize missing ingredients (2) first.
    # ignorePantry - Whether to ignore typical pantry items, such as water, salt, flour, etc.
    querystring = {
        "diet": diet,
        "type": meal_type,
        "includeIngredients": ingredients,
        "ignorePantry": "true",
        # "cuisine": cuisine,
        "maxReadyTime": max_ready_time,
        "number": number,
    }

    headers = {
        "X-RapidAPI-Key": "fad3c2e0d1mshac32fe2d91a63fdp12595bjsncf3b07bd3765",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()

    return data["results"]


def get_random_recipe(recipes):
    recipe_number = random.randint(0, len(recipes))
    id = recipes[recipe_number]["id"]

    url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/information"
    headers = {
        "X-RapidAPI-Key": "fad3c2e0d1mshac32fe2d91a63fdp12595bjsncf3b07bd3765",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()

    recipe_data = {
        "title": data["title"],
        "image": data["image"],
        "servings": data["servings"],
        "readyInMinutes": data["readyInMinutes"],
        "cuisines": data["cuisines"],
        "diets": data["diets"],
        "dishTypes": data["dishTypes"],
        "extendedIngredients": data["extendedIngredients"],
        "summary": data["summary"],
        "winePairing": data["winePairing"]
    }

    return recipe_data


if __name__ == "__main__":
    main()
