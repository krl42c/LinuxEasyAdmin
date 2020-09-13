from LEA import app,resources
from flask import render_template

@app.route('/')
def index():
    return render_template('base.html',title='INICIO')


