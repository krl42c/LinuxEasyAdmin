from LEA import app,resources
from flask import render_template

@app.route('/')
def index():
    return render_template('base.html',title='INICIO',processList=resources.getProcessList(), mem=resources.getMem(),os=resources.getOS())


@app.route('/ram')
def ram():
    return render_template('ram.html',ram_percent=resources.getRAMUsagePercent())

