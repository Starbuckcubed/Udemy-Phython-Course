from flask import Flask
import json
#always needed whether a FLask app or API
app = Flask(__name__)

#data for the API
recipes = {
    1: {'id': 1, 'title': 'Spaghetti Carbonara', 'ingredients': ['spaghetti', 'eggs', 'pecorino cheese', 'guanciale'], 'instructions': 'Cook pasta, fry guanciale, mix with eggs and cheese, and combine with pasta.'},
    2: {'id': 2, 'title': 'Tomato Soup', 'ingredients': ['tomato', 'water', 'salt'], 'instructions': 'Boil all together until mushy, blend, and serve.'},
    3: {'id': 3, 'title': 'Grilled Cheese Sandwich', 'ingredients': ['bread', 'cheese', 'butter'], 'instructions': 'Butter bread, place cheese between slices, grill until golden.'}
}
# <int:recipe_id> parameter in the route ensures that recipe_id is automatically handled as an integer
#specifies that this route only responds to GET requests
@app.route('/recipes/<int:recipe_id>' , methods=['GET'])
#function
def get_recipe(recipe_id):
    recipe = recipes.get(recipe_id)
    if recipe:
        return recipe
    else:
        return {'message':'No recipe found'}, 404
    #Homepage route
@app.route('/')
def index():
    return "Recipe Search Homepage"

app.run(debug=True)