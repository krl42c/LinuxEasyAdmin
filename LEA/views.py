from LEA import app, resources, users
from flask import render_template
from jinja2 import TemplateNotFound

INTERNAL_ERROR = "500: Internal server error"


@app.route('/')
def index():
    try:
        return render_template('index.html', title='INICIO', os=resources.get_os())
    except TemplateNotFound:
        return INTERNAL_ERROR, 500


@app.route('/ram')
def ram():
    try:
        return render_template('ram.html', ram_percent=resources.get_ram_usage_percent())
    except TemplateNotFound:
        return INTERNAL_ERROR, 500


@app.route("/users")
def list_users():
    try:
        return render_template('users.html', user_list=users.get_users())
    except TemplateNotFound:
        return INTERNAL_ERROR, 500


@app.route("/users/<user>")
def user_info(user):
    try:
        return render_template('user_info.html', user=user, user_groups=users.get_user_groups(user))
    except TemplateNotFound:
        return INTERNAL_ERROR, 500


@app.route("/users/create_user/<user>")
def create_user(user):
    users.create_user(user)


@app.route("/users/delete_user/<user>")
def delete_user(user):
    users.delete_user(user)


@app.route("/packages")
def packages():
    pass


@app.route("/packages/install_package/<package>")
def install_package(package):
    pass


@app.route("/packages/delete_package/<package>")
def delete_package(package):
    pass


@app.route("/process")
def process():
    print("Rendering 'process.html'...")
    try:
        return render_template('process.html', processList=resources.get_process_list())
    except TemplateNotFound:
        print("Template not found exception raised")
        return INTERNAL_ERROR, 500


@app.route("/process/start_process/<name>")
def start_process(name):
    pass


@app.route("/process/stop_process/<name>")
def stop_process(name):
    # TODO: Implement process stopping
    print("Stopped process " + name)
    try:
        return render_template('process.html', processList=resources.get_process_list())
    except TemplateNotFound:
        print("Template not found exception raised")
        return INTERNAL_ERROR, 500


@app.route("/process/details/<name>")
def process_details(name):
    pass
