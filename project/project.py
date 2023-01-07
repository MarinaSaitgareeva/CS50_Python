import requests
import random




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