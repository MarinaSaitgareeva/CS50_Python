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