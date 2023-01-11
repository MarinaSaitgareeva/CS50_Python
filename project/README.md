# Random Recipe Picker

---

### Video Demo: <URL HERE>

### Description:

The Final project is done as a part of the CS50’s Introduction to Programming with Python course by Harvard:
Random Recipe Picker based on the preferred diet type, meal type, ingredients and maximum cooking time.

![PDF Example] (/Users/marinas/projects/CS50_Python/project/Example_PDF.png)

### Run the Random Recipe Picker:

1. **Python 3.11** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **PIP Dependencies** - Once your Python is installed, install the required dependencies by navigating to the `/project` directory and running:

```bash
pip install -r requirements.txt
python project.py
```

---

### Functions:

It contains the main function as well as other ones which were a requirement in the course specification:

1.  <details>
    <summary> import </summary>
    <p> - requests </p>
    <p> - random </p>
    <p> - fpdf </p>
    <p> - sys </p>
    <p> - os </p>
    <p> - mimetypes </p>
    </details>

2.  <details>
    <summary> def main(): </summary>
    <p> - Get the diet, meal type, ingredients, max ready time from the user. </p>
    <p> - Get Recipes from the API. </p>
    <p> - Select Random Recipes from the Recipes list. </p>
    <p> - Save it in the PDF file. </p>
    </details>

3.  <details>
    <summary> def get_diet(): </summary>
    <p> - Ask the user to "Select diet type". </p>
    </details>

4.  <details>
    <summary> def get_meal_type(): </summary>
    <p> - Ask the user to "Select meal type". </p>
    </details>

5.  <details>
    <summary> def get_ingredients(): </summary>
    <p> - Ask the user "A comma-separated list of ingredients that the recipes should contain". </p>
    </details>

6.  <details>
    <summary> def get_max_ready_time(): </summary>
    <p> - Ask the user "The maximum time in minutes it should take to prepare and cook the recipe". </p>
    </details>

7.  <details>
    <summary> def get_recipes(): </summary>
    <p> - Get Recipes from API based on the diet, meal type, ingredients, max ready time, and number. </p>
    </details>

8.  <details>
    <summary> def get_random_recipe(recipes): </summary>
    <p> - Get the Recipe from the Recipes list based on the random number. </p>
    <p> - Save each ingredient in the list. </p>
    </details>

9.  <details>
    <summary> def get_recipe_instructions(recipe_id): </summary>
    <p> - Get the Recipe instructions from API based on the recipe's ID. </p>
    <p> - Save each step in the list. </p>
    </details>

10. <details>
    <summary> class PDF: </summary>
    <p> Class is used for saving Random Recipe in the PDF file. </p>
    <p> PDF file includes Title, Servings, Ready Time in Minutes, Image, Ingredients list, and Recipe instructions. </p>
    <p> Save function is used to save PDF files with the name: Recipe Title. </p>
    </details>

11. <details>
    <summary> def save_recipe_in_pdf(recipe): </summary>
    <p> Ask if the user wants to save Random Recipe. </p>
    <p> Save the recipe's image in the current project folder with name = id.extension. </p>
    <p> Save extended_ingredients and recipe_instructions in the string instead of the list. </p>
    <p> Create and save PDF with the Recipe. </p>
    <p> Delete the recipe's image in the current project folder with name = id.extension. </p>
    <p> Delete font file. </p>
    </details>

---

### Test functions: test_project.py

It performs basic tests on the main file that can be executed via pytest.

```bash
pytest test_project.py
```
