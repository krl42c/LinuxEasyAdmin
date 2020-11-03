# LINUX EASY ADMIN

## Instalación 

```
# apt install python3 python3-pip python3-venv gcc
# ./init_script.sh
# flask run
```


## API USAGE

### Users

Get a list of users

```
GET /api/users
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


