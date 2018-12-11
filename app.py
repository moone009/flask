from flask import (Flask, render_template, redirect,
                   url_for, request, make_response)
import json
from options import DEFAULTS

app = Flask(__name__)

def get_saved():
  try:
	    data = json.loads(request.cookies.get('character'))
  except TypeError:
	    data = {}
  return(data)	

@app.route('/')
def index():
  return render_template("index.html",saves=get_saved())

@app.route('/builder')
def builder():
  return render_template("builder.html",saves=get_saved(),options=DEFAULTS)

@app.route('/save',methods=['POST'])
def save():
  response = make_response(redirect(url_for('builder')))
  data = get_saved()
  data.update(dict(request.form.items()))
  response.set_cookie('character',json.dumps(data))
  #import pdb; pdb.set.trace()
  return(response)

app.run(debug=True)