from LEA import app, resources, users, apiresponse
from simplepam import authenticate
from flask import render_template, session, redirect, url_for, escape, request
from jinja2 import TemplateNotFound
import json

INTERNAL_ERROR = "500: Internal server error"

app.config.from_json('settings.json')

@app.route('/')
def index():
    try:
        return render_template('index.html', title='INICIO', os=resources.get_os())
    except TemplateNotFound:
        return INTERNAL_ERROR, 500

@app.route('/api/create_user', methods=['POST'])
def api_create_user():
    content = request.json
    print(content)
    users.create_user(content['username'], content['auth'])
    response = apiresponse.APIResponse()
    response.insert_value("Status", "OK")
    response.insert_value("Message", "User " + content['username'] + " created")
    return response.get_json_response()

@app.route("/api/delete_user", methods=["POST"])
def api_delete_user():
    content = request.json
    print(content)
    return users.delete_user(content['username'])


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate(username,password):
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            return 'Invalid username/password'
    return '''
           <form action="" method="post">
               <p><input type=text name=username>
               <p><input type=password name=password>
               <p><input type=submit value=Login>
           </form>
       '''

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))


@app.route('/ram')
def ram():
    try:
        return render_template('ram.html', ram_percent=resources.get_ram_usage_percent())
    except TemplateNotFound:
        return INTERNAL_ERROR, 500


@app.route("/api/ram")
def api_ram():
    return { "Usage" : resources.get_ram_usage_percent()}

@app.route("/users")
def list_users():
    try:
        return render_template('users.html', user_list=users.get_users())
    except TemplateNotFound:
        return INTERNAL_ERROR, 500



@app.route("/api/users/<user>")
def api_get_user(user):
    return { user : users.get_user_groups(user) }

@app.route("/api/users")
def get_user_list():
    user_list = users.get_users()
    # return { "users" : json.dumps(user_list) }
    return json.dumps(user_list)

@app.route("/users/<user>")
def user_info(user):
    try:
        return render_template('user_info.html', user=user, user_groups=users.get_user_groups(user))
    except TemplateNotFound:
        return INTERNAL_ERROR, 500



@app.route("/api/process")
def api_process_list():
    return json.dumps(resources.get_process_list())


@app.route("/users/create_user")
def create_user():
    try:
        return render_template('create_user.html')
    except TemplateNotFound:
        return INTERNAL_ERROR, 500

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


if __name__ == "__main__":
    app.run(debug=True)
