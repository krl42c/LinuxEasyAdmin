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



