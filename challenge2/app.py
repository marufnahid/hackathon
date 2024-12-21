from flask import Flask, request, jsonify
from database import init_db
from recipe import add_recipe, search_recipes, get_all_recipes
from chatbot import get_recipe_suggestion
from ingredient_management import add_ingredient, get_ingredients, update_ingredient

app = Flask(__name__)

# Initialize the database schema
init_db()

# Ingredient Management Routes
@app.route("/ingredients", methods=["POST"])
def add_ingredient_route():
    return add_ingredient()

@app.route("/ingredients", methods=["GET"])
def get_ingredients_route():
    return get_ingredients()

@app.route("/ingredients/<int:id>", methods=["PUT"])
def update_ingredient_route(id):
    return update_ingredient(id)

# Recipe Management Routes
@app.route("/recipes", methods=["POST"])
def add_recipe_route():
    return add_recipe()

@app.route("/recipes/search", methods=["GET"])
def search_recipes_route():
    return search_recipes()

@app.route("/recipes", methods=["GET"])
def get_all_recipes_route():
    return get_all_recipes()

# Chatbot Route for Recipe Suggestions
@app.route("/chatbot", methods=["GET"])
def chatbot_route():
    return get_recipe_suggestion()

if __name__ == "__main__":
    app.run(debug=True)
