import projects #projects definitions are placed in different file


@app.route("/Signup")
def Signup():
  return render_template("Sign-up.html")

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to render home.html
@app.route('/')
def home_route():
  return render_template("home.html", projects=projects.setup())

#connects /hello path of server to render comediandecades.html
@app.route('/comediandecades/')
def comediandecades_route():
  return render_template("comediandecades.html", projects=projects.setup())

#connects /historyofcomedy path of server to render historyofcomedy.html
@app.route('/historyofcomedy/')
def historyofcomedy_route():
  return render_template("historyofcomedy.html", projects=projects.setup())

#connects /knock path of server to render knock.html
@app.route('/knock')
def knock_route():
  return render_template("knock.html", projects=projects.setup())
  
#connects /iniyaa path of server to render iniyaa.html
@app.route('/iniyaa')
def iniyaa_route():
  return render_template("iniyaa.html", projects=projects.setup())

#connects /ketki path of server to render ketki.html
@app.route('/ketki')
def ketki_route():
  return render_template("ketki.html", projects=projects.setup())

#connects /ava path of server to render ava.html
@app.route('/ava')
def ava_route():
  return render_template("ava.html", projects=projects.setup())

#connects /lucas path of server to render lucas.html
@app.route('/lucas')
def lucas_route():
  return render_template("lucas.html", projects=projects.setup())

#connects /submit path of server to render submit.html
@app.route('/submit')
def submit_route():
  return render_template("submit.html", projects=projects.setup())

@app.route("/playground")
def playground_route():
  return render_template("playground.html")


if __name__ == "__main__":
  app.run(debug=True, port='3000', host='127.0.0.1') #192.168.1.228