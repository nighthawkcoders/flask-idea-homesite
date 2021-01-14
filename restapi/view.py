from flask import render_template
from restapi import restapi_bp
from models.lessons import menus
import requests

# connects default URL to a function
@restapi_bp.route('/',  methods=['GET', 'POST'])
def joke():
    # call to random joke web api
    url = 'https://official-joke-api.appspot.com/jokes/programming/random'
    resp = requests.get(url)
    # formatting variables from return
    setup = resp.json()[0]['setup']
    punchline = resp.json()[0]['punchline']
    return render_template("restapi/index.html", menus=menus,  setup=setup, punchline=punchline)
