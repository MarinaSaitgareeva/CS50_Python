import requests
import random
from fpdf import FPDF
import sys
import os


def main():
    while True:
        diet = get_diet()
        meal_type = get_meal_type()
        ingredients = get_ingredients()
        max_ready_time = get_max_ready_time()

        try:
            recipes = get_recipes(
                diet,
                meal_type,
                ingredients,
                max_ready_time,
                100
            )
            recipe = get_random_recipe(recipes)
            print(f"\n Recipe title: {recipe['title']}")
            save_recipe_in_pdf(recipe)

        except Exception as e:
            print(e)
            continue


def get_diet():
    while True:
        available_diets = [
            "None",
            "Gluten Free",
            "Ketogenic",
            "Vegetarian",
            "Lacto-Vegetarian",
            "Ovo-Vegetarian",
            "Vegan",
            "Pescetarian",
            "Paleo",
            "Primal",
            "Low FODMAP",
            "Whole30"
        ]

        selected_diet = input(
            "\n Select diet type: \n \
            1. None \n \
            2. Gluten Free\n \
            3. Ketogenic \n \
            4. Vegetarian \n \
            5. Lacto-Vegetarian \n \
            6. Ovo-Vegetarian \n \
            7. Vegan \n \
            8. Pescetarian \n \
            9. Paleo \n \
            10. Primal \n \
            11. Low FODMAP \n \
            12. Whole30 \n \
            Your diet type: "
        ).strip()

        try:
            if not selected_diet:
                return ""
            elif 0 < int(selected_diet) < 13:
                return available_diets[int(selected_diet) - 1]

        except Exception:
            continue


def get_meal_type():
    while True:
        available_meal_type = [
            "none",
            "main course",
            "side dish",
            "dessert",
            "appetizer",
            "salad",
            "bread",
            "breakfast",
            "soup",
            "beverage",
            "sauce",
            "marinade",
            "fingerfood",
            "snack",
            "drink"
        ]
        selected_meal_type = input(
            "\n Select meal type: \n \
            1. None \n \
            2. Main course \n \
            3. Side dish \n \
            4. Dessert \n \
            5. Appetizer \n \
            6. Salad \n \
            7. Bread \n \
            8. Breakfast \n \
            9. Soup \n \
            10. Beverage \n \
            11. Sauce \n \
            12. Marinade \n \
            13. Fingerfood \n \
            14. Snack \n \
            15. Drink \n \
            Your meal type: "
        ).strip()

        try:
            if not selected_meal_type:
                return ""
            elif 0 < int(selected_meal_type) < 15:
                return available_meal_type[int(selected_meal_type) - 1]

        except Exception:
            continue


def get_ingredients():
    while True:
        ingredients = input(
            "\n A comma-separated list of ingredients that the recipes should contain: "
            ).strip()

        if (not ingredients) or ingredients.isnumeric():
            continue
        return ingredients.lower()


def get_max_ready_time():
    while True:
        max_ready_time = input(
            "\n The maximum time in minutes it should take to prepare and cook the recipe: "
            ).strip()

        try:
            return int(max_ready_time)

        except Exception:
            continue


def get_recipes(diet, meal_type, ingredients, max_ready_time, number):
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"

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
    print(f"{recipe_number} in {len(recipes)} recipes")
    id = recipes[recipe_number]["id"]

    url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/information"
    headers = {
        "X-RapidAPI-Key": "fad3c2e0d1mshac32fe2d91a63fdp12595bjsncf3b07bd3765",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()

    recipe_ingredients = []

    for ingredient in data["extendedIngredients"]:
        ingredient_data = {
            "name": ingredient["name"],
            "original": ingredient["original"],
            "id": ingredient["id"],
            "image": ingredient["image"],
            "amount": ingredient["amount"],
            "unit": ingredient["unit"],
            "original": ingredient["original"],
            }
        recipe_ingredients.append(ingredient_data)

    recipe_instructions = get_recipe_instructions(id)

    recipe_data = {
        "id": data["id"],
        "title": data["title"],
        "image": data["image"],
        "servings": data["servings"],
        "readyInMinutes": data["readyInMinutes"],
        # "cuisines": data["cuisines"],
        # "diets": data["diets"],
        # "dishTypes": data["dishTypes"],
        "extendedIngredients": recipe_ingredients,
        # "summary": data["summary"],
        "winePairing": data["winePairing"],
        # "sourceUrl": data["sourceUrl"],
        "recipe_instructions": recipe_instructions,
    }

    return recipe_data


def get_recipe_instructions(recipe_id):
    url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{recipe_id}/analyzedInstructions"

    querystring = {"stepBreakdown":"true"}

    headers = {
        "X-RapidAPI-Key": "fad3c2e0d1mshac32fe2d91a63fdp12595bjsncf3b07bd3765",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()

    recipe_instructions = []

    for step in data[0]["steps"]:
        step = {
            "number": step["number"],
            "step": step["step"],
        }

        recipe_instructions.append(step)

    return recipe_instructions


class PDF:
    def __init__(self, id, title, servings, readyInMinutes, extendedIngredients, recipe_instructions):
        # By default, a FPDF document has a A4 format with
        # portrait orientation (orientation="portrait", format="A4").
        self._pdf = FPDF(orientation="P", unit="mm", format="A4")
        self._pdf.add_page()
        
        # Setting color: white.
        # self._pdf.set_text_color(255, 255, 255)
        # Setting font: GoodUnicornRegular 40.
        self._pdf.add_font("GoodUnicornRegular-Rxev", "", "GoodUnicornRegular-Rxev.ttf", uni=True)
        self._pdf.set_font("GoodUnicornRegular-Rxev", size=30)
        # Printing title.
        self._pdf.multi_cell(
            w=0, h=10, txt=f"{title.strip().capitalize()}", align="C",
        )
        # Setting font: Arial 8.
        self._pdf.set_font("Arial", size=8)
        # Printing servings + readyInMinutes.
        self._pdf.cell(
            w=0,
            h=8,
            txt=f"for {servings} servings - ready in {readyInMinutes} ",
            align="C",
            ln = 1,
        )
        # Adding image.
        self._pdf.image(f"{id}.jpeg", w=50, h=50, x=80, y=40)
        # Move cursor down after the image.
        self._pdf.set_y(100)
        # Setting font: Arial 8.
        self._pdf.set_font("Arial", size=8)
        # Printing extendedIngredients + recipe_instructions.
        self._pdf.multi_cell(
            w=0,
            h=6,
            txt=f"{extendedIngredients} \n {recipe_instructions}",
            align="L",
        )


    def save(self, title):
        title = f"{title.replace(' ', '_')}.pdf"
        self._pdf.output(title)


def save_recipe_in_pdf(recipe):
    while True:
        save_recipe = input("\n Do you want to save recipe? (yes or no): ").strip().lower()

        if save_recipe not in ["yes", "no"]:
            continue 

        elif save_recipe == "yes":
            id = recipe["id"]
            title = recipe["title"]
            img_data = requests.get(recipe["image"]).content
            with open(f"{id}.jpeg", "wb") as handler:
                handler.write(img_data)

            servings = recipe["servings"]
            readyInMinutes = f"{recipe['readyInMinutes']} min"

            extendedIngredients = "Ingredients: \n"
            for extendedIngredient in recipe["extendedIngredients"]:
                extendedIngredients += f"{extendedIngredient['original']} \n"

            recipe_instructions = "Recipe instructions: \n"
            for recipe_instruction in recipe["recipe_instructions"]:
                recipe_instructions += f"{recipe_instruction['number']}. {recipe_instruction['step']} \n"
            
            print(recipe)
            
            pdf = PDF(id, title, servings, readyInMinutes, extendedIngredients, recipe_instructions)
            pdf.save(title)

            os.remove(f"{id}.jpeg")
            os.remove("GoodUnicornRegular-Rxev.pkl")

            sys.exit()

        elif save_recipe == "no":
            try_again = input("\n Do you want to try again? (yes, no): ").strip().lower()

            if try_again == "yes":
                main()
            else:
                sys.exit()
    

if __name__ == "__main__":
    main()
