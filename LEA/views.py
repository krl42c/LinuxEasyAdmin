from LEA import app,resources
from flask import render_template

@app.route('/')
def index():
    return render_template('base.html',title='INICIO',processList=resources.get_process_list(), mem=resources.get_ram(),os=resources.get_os())


@app.route('/ram')
def ram():
    return render_template('ram.html',ram_percent=resources.get_ram_usage_percent())

