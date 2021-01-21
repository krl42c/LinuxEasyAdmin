from LEA import app, resources, users, apiresponse, actions, packages, process
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
    response = apiresponse.APIResponse()
    if users.create_user(content['username'], content['auth']):
        response.insert_value("Status", "OK")
        response.insert_value("Message", "User " + content['username'] + " created")
    else:
        response.insert_value("Error", "Couldn't create user")
    return response.get_json()


@app.route("/api/delete_user", methods=["POST"])
def api_delete_user():
    content = request.json
    response = apiresponse.APIResponse()
    if users.delete_user(str(content['username']['s']['s'])):  # Will return 1 if user hasn't been created
        response.insert_value("Status", "OK")
    else:
        response.insert_value("Error", "Couldn't delete user")
    return response.get_json()


@app.route("/api/change_password", methods=["POST"])
def api_change_password():
    content = request.json
    user = content['username']
    new_pass = content['new_password']
    old_pass = content['old_pass']
    # TODO: Implement function in users.py
    response = apiresponse.APIResponse()
    response.insert_value("Status", "OK")
    return response.get_json()


@app.route('/api/login', methods=['POST'])
def login():
    content = request.json
    ip = content['ip']
    password = content['password']

    response = apiresponse.APIResponse()
    response.insert_value("IP", str(ip))
    return response.get_json()



@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/ram')
def ram():
    try:
        return render_template('ram.html', ram_percent=resources.get_ram_usage_percent())
    except TemplateNotFound:
        return INTERNAL_ERROR, 500


@app.route("/api/ram")
def api_ram():
    response = apiresponse.APIResponse()
    response.insert_value("Value", resources.get_ram_usage_percent())
    return response.get_json()


@app.route("/users")
def list_users():
    try:
        return render_template('users.html', user_list=users.get_users())
    except TemplateNotFound:
        return INTERNAL_ERROR, 500


@app.route("/api/users/<user>")
def api_get_user(user):
    return {user: users.get_user_groups(user)}


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

@app.route("/api/stop_process", methods=['POST'])
def api_stop_process():
    content = request.json
    response = apiresponse.APIResponse()
    process_name = content["name"]["s"]
    if "|" in process_name or "&" in process_name:
        response.insert_value("Status", "Error")
        return response.get_json(),400

    if process.delete_process(str(process_name)):
        response.insert_value("Status", "OK")
        return response.get_json()
    else:
        response.insert_value("Status", "Error")
        return response.get_json(),400


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


@app.route("/api/cpu")
def api_get_cpu():
    response = apiresponse.APIResponse()
    response.insert_value("Value", resources.get_cpu_usage())
    return response.get_json()


@app.route("/api/package/install", methods=["POST"])
def api_install_package():
    content = request.json

    response = apiresponse.APIResponse()

    package_name = content["name"]
    pkgManager = packages.PackageManager("yum")
    if "|" in package_name or "&" in package_name:
        response.insert_value("Status", "Error")
        return response.get_json(), 400

    if pkgManager.install(package_name):
        response.insert_value("Status", "OK")
        return response.get_json(), 200
    else:
        response.insert_value("Status", "Erorr")
        return response.get_json(), 400


@app.route("/api/package/delete", methods=["POST"])
def api_delete_package():
    content = request.json
    response = apiresponse.APIResponse()

    package_name = content["name"]['s']
    print(package_name)
    pkgManager = packages.PackageManager("yum")

    if pkgManager.remove(package_name):
        response.insert_value("Status", "OK")
        return response.get_json(), 200
    else:
        response.insert_value("Status", "Error")
        return response.get_json(), 400

@app.route("/api/package/status")
def api_package_status():
    response = apiresponse.APIResponse()
    if resources.apt_locked() == b'FREE':
        response.insert_value("Status","Free")
        return response.get_json(),200
    else:
        response.insert_value("Status","Locked")
        return  response.get_json(),200


@app.route("/api/battery")
def api_battery():
    response = apiresponse.APIResponse()
    response.insert_value("Plug", resources.get_battery_plugged())
    response.insert_value("Value", resources.get_battery_percentage())
    return response.get_json(), 200


@app.route("/api/shutdown")
def api_shutdown():
    response = apiresponse.APIResponse()
    response.insert_value("Value", "Ok")
    actions.shutdown()
    return response.get_json(), 200


@app.route("/api/disk")
def api_disk():
    response = apiresponse.APIResponse()
    response.insert_value("Value", resources.get_disk_space())
    return response.get_json(), 200

@app.route("/api/disk_folders")
def api_disk_folders():
    return json.dumps(resources.get_disk_folders()),200

@app.route("/api/ram/process")
def api_ram_process():
    return json.dumps(resources.get_process_list_with_usage()),200

@app.route("/api/package/list")
def api_package_list():
    return json.dumps(resources.installed_packages()),200

if __name__ == "__main__":
    app.run(debug=True)
