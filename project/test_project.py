import pytest
from project import (
    get_diet,
    get_meal_type,
    get_ingredients,
    get_max_ready_time,
    get_recipes,
    get_random_recipe,
    get_recipe_instructions,)
import mock
import builtins


def test_get_diet():
    # Correct diet type number
    with mock.patch.object(builtins, "input", lambda _: "2"):
        assert get_diet() == "Gluten Free"
    # Empty diet type number
    with mock.patch.object(builtins, "input", lambda _: ""):
        assert get_diet() == ""
    # Type diet type number out of range
    with mock.patch.object(builtins, "input", lambda _: "14") and pytest.raises(Exception):
        get_diet()
    # Type incorrect diet type number (not number < 13)
    with mock.patch.object(builtins, "input", lambda _: "diet") and pytest.raises(Exception):
        get_diet()


def test_get_meal_type():
    # Correct meal type number
    with mock.patch.object(builtins, "input", lambda _: "2"):
        assert get_meal_type() == "main course"
    # Empty meal type number
    with mock.patch.object(builtins, "input", lambda _: ""):
        assert get_meal_type() == ""
    # Type meal type number out of range
    with mock.patch.object(builtins, "input", lambda _: "16") and pytest.raises(Exception):
        get_meal_type()
    # Type incorrect meal type number (not number < 13)
    with mock.patch.object(builtins, "input", lambda _: "meal") and pytest.raises(Exception):
        get_meal_type()


def test_get_ingredients():
    # Correct ingredients list
    with mock.patch.object(builtins, "input", lambda _: "chicken, apple"):
        assert get_ingredients() == "chicken, apple"
    # Empty ingredients
    with mock.patch.object(builtins, "input", lambda _: "") and pytest.raises(Exception):
        get_ingredients()
    # Type number instead of alphabetic
    with mock.patch.object(builtins, "input", lambda _: "123") and pytest.raises(Exception):
        get_ingredients()


def test_get_max_ready_time():
    # Correct max ready time
    with mock.patch.object(builtins, "input", lambda _: "20"):
        assert get_max_ready_time() == 20
    # Incorrect max ready time (not number)
    with mock.patch.object(builtins, "input", lambda _: "ten") and pytest.raises(Exception):
        get_max_ready_time()
    # Empty max ready time
    with mock.patch.object(builtins, "input", lambda _: "") and pytest.raises(Exception):
        get_max_ready_time()


def test_get_recipes():
    assert len(get_recipes("", "", "chicken", 40, 100)) > 0


def test_get_random_recipe():
    recipe = get_random_recipe(get_recipes("", "", "chicken", 40, 100))
    assert type(recipe) is dict
    assert "recipe_instructions" in recipe.keys()


def test_get_recipe_instructions():
    recipe_id = 753644
    assert len(get_recipe_instructions(recipe_id)) > 0

