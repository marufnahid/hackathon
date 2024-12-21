from database import execute_query, fetch_query
from flask import request, jsonify

# Add a new ingredient to the database
def add_ingredient():
    data = request.json
    query = "INSERT INTO ingredients (name, quantity) VALUES (?, ?)"
    try:
        execute_query(query, (data['name'], data['quantity']))
        return jsonify({"message": "Ingredient added successfully!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Ingredient already exists!"}), 400

# Get all ingredients from the database
def get_ingredients():
    query = "SELECT * FROM ingredients"
    results = fetch_query(query)
    return jsonify(results)

# Update the quantity of an ingredient in the database
def update_ingredient(id):
    data = request.json
    query = "UPDATE ingredients SET quantity = ? WHERE id = ?"
    execute_query(query, (data['quantity'], id))
    return jsonify({"message": "Ingredient updated successfully!"})
