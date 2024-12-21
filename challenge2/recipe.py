from database import execute_query, fetch_query
from flask import request, jsonify

# Add a new recipe to the database
def add_recipe():
    data = request.json
    query = """
    INSERT INTO recipes (name, ingredients, taste, reviews, cuisine, preparation_time, recipe_text) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    try:
        execute_query(query, (
            data['name'], 
            data['ingredients'], 
            data['taste'], 
            data['reviews'], 
            data['cuisine'], 
            data['preparation_time'], 
            data['recipe_text']
        ))
        return jsonify({"message": "Recipe added successfully!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Recipe already exists!"}), 400

# Search for recipes based on ingredients
def search_recipes():
    available_ingredients = request.args.get('ingredients')
    query = """
    SELECT * FROM recipes WHERE ingredients LIKE ?
    """
    recipes = fetch_query(query, ('%' + available_ingredients + '%',))
    return jsonify(recipes)

# Retrieve all recipes
def get_all_recipes():
    query = "SELECT * FROM recipes"
    recipes = fetch_query(query)
    return jsonify(recipes)
