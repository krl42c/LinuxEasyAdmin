from LEA import app, resources, users, apiresponse, actions, packages
from simplepam import authenticate
from flask import render_template, session, redirect, url_for, escape, request
from jinja2 import TemplateNotFound
import json
import psutil
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
    print(content)
    if users.delete_user(content['username']): #Will return 1 if user hasn't been created
        response.insert_value("Status","OK")
        response.insert_value("Message","User " + content['username'] + " has been deleted")
    else:
        response.insert_value("Error", "Couldn't delete user")
    return response.get_json()

@app.route("/api/chage_password", methods=["POST"])
def api_change_password():
	content = request.json
	user = content['username']
	new_pass = content['new_password']
	old_pass = content['old_pass']
	#TODO: Implement function in users.py
	response = apiresponse.APIResponse()
	response.insert_value("Status", "OK")
	return response.get_json()

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

@app.route("/api/cpu")
def api_get_cpu():
    response = apiresponse.APIResponse()
    response.insert_value("Value", resources.get_cpu_usage())
    return response.get_json(),400

@app.route("/api/package/install", methods=["POST"])
def api_install_package():
    content = request.json

    response = apiresponse.APIResponse()

    package_name = content["name"]
    pkgManager = packages.PackageManager("apt")
    if "|" in package_name or "&" in package_name:
        response.insert_value("Status", "Error")
        return response.get_json(),400

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

	package_name = content["name"]
	pkgManager = packages.PackageManager("apt")

	if pkgManager.delete(package_name):
		response.insert_value("Status","OK")
		return response.get_json(),200
	else:
		response.insert_value("Status", "Error")
		return response.get_json(),400

@app.route("/api/packages")
def api_packages():
	#TODO: implement in packages.py
	pass

@app.route("/api/battery")
def api_battery():
	response = apiresponse.APIResponse()
	response.insert_value("Value", resources.get_battery_percentage())
	return response.get_json(), 200

@app.route("/api/shutdown")
def api_shutdown():
	actions.shutdown()
	return 200

@app.route("/api/disk")
def api_disk():
    response = apiresponse.APIResponse()
    response.insert_value("Value", resources.get_disk_space())
    return response.get_json(), 200

if __name__ == "__main__":
    app.run(debug=True)
