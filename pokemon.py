### app.py:

from flask import Flask, render_template
from helper import get_random_pokemon_selection, get_pokemon_info

app = Flask(__name__)

@app.route("/")
def pokemon_selection():
    random_pokemon_selection = get_random_pokemon_selection()
    return render_template("pokemon_selection.html", random_pokemon_selection=random_pokemon_selection)

@app.route("/<name>")
def pokemon_info(name):
    pokemon = get_pokemon_info(name.lower())  # Convert the name to lowercase
    return render_template("pokemon_info.html", pokemon=pokemon)

app.run(debug=True)
