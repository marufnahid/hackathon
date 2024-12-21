# import openai
from openai import OpenAI
from flask import request, jsonify
from config import OPENAI_API_KEY  # Ensure that your API key is in the config file

# openai.api_key = OPENAI_API_KEY

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=OPENAI_API_KEY,
)

# Function to call OpenAI's GPT-3 for recipe suggestions
def get_recipe_suggestion():
    craving = request.args.get('craving')  # Get the craving from the query parameter
    ingredients = request.args.get('ingredients')  # Get the ingredients from the query parameter
    
    # Ensure the required parameters are provided
    if not craving or not ingredients:
        return jsonify({"error": "Both 'craving' and 'ingredients' must be provided as query parameters"}), 400
    
    # Prepare the prompt for OpenAI's model
    prompt = f"Suggest a recipe based on the following ingredients: {ingredients}. The user is craving: {craving}."
    
    try:
        # Call the OpenAI API to get a recipe suggestion using the new chat completions method
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use the GPT model of your choice (e.g., gpt-3.5-turbo, gpt-4)
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        
        # Return the recipe suggestion from the response
        return jsonify({"suggested_recipe": response.choices[0].message.content.strip()})
    
    except client.OpenAIError as e:
        # Catch errors related to OpenAI API (use the new error class)
        return jsonify({"error": f"OpenAI API error: {str(e)}"}), 500
    except Exception as e:
        # Catch any other unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500
