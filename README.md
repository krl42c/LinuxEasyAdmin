# LINUX EASY ADMIN

## Instalación 

```
# apt install python3 python3-pip python3-venv gcc
# ./init_script.sh
# flask run
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


