# LINUX EASY ADMIN

Linux Easy Admin is an open-source tool used to manage GNU/Linux systems.

This repository only contains the API, written in Python using Flask.

You can use the API as it is, build your own front-end, or use [lea-front](https://www.github.com/krl42c/lea-front).


## INSTALLATION 


### DEPENDENCIES 

On Ubuntu 18.04
```
# apt install python3 python3-pip python3-venv gcc
```

### SETUP

You can run the init script from your shell:
```
# ./init_script.sh
```

This will setup a python virtual environment and install the required packages for LEA to work.

If you want to do it manually:
```
# python3 -m venv venv
# . venv/bin/activate
# pip install -e .
```

### RUNNING

Run the following inside your shell from the top directory of the repo and the server will start working:
```
# export FLASK_APP=LEA
# flask run
```

You can set the host/port by running the program as:
```
# flask run --host=x --port=y
```


## API USAGE

---	

### USERS

Get a list of users

```
GET /api/users
```

Get information from a specific user

```
GET /api/user/<user>
``` 

Create a new user

```
POST /api/create_user
```

Send the following body 

```json
{ 
    "username" : "username",
    "auth" : "password"
}
```

Delete an user

```
POST /api/delete_user
```

```json
{
    "username" : "username",
    "auth" : "auth"
}
```
---

### RESOURCES

Get disk space

```
GET /api/disk/<disknumber>
``` 

Get RAM usage

``` 
GET /api/ram
```

Get CPU usage

``` 
GET /api/cpu
```

Get battery percent

``` 
GET /api/battery
```

Get folders with disk usage

``` 
GET /api/disk/folders
```

Get process list with ram usage

``` 
GET /api/ram/process
```

Shutdown

``` 
GET /api/shutdown
```

--- 

### PACKAGES

Get package manager lock status 

``` 
GET /api/package/status
```

Install package 

``` 
POST /api/package/install
```

```json
{
    "name" : "name",
}
```

Delete package

``` 
POST /api/package/delete
```

```json
{
    "name" : "name",
}
```


### PROCESS MANAGEMENT


Get process list 

``` 
GET /api/process
```

Shutdown process

``` 
GET /process/stop_process/<name>
```


