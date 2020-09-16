# API Documentation

### `POST /user/create`
 Creates a new user

* **Request Body** : JSON Object with following keys

```JS
{
    "name":"string",
    "email":"string",
    "address": {
        "line1":"string",
        "line2":"string",
        "locality":"string",
        "city":"string",
        "state":"string",
        "pin":"string"
    }
}
```

**Required keys :** 
* name 
* email 

**Response :** 
* returns id of user


### `POST /worker/create`
Creates a new worker

* **Request Body** : JSON Object with following keys

```JS
{
    "name":"string",
    "username":"string",
    "age":"number",
    "gender":"string",
    "address": {
        "line1":"string",
        "line2":"string",
        "locality":"string",
        "sity":"string",
        "state":"string",
        "pin":"string"
    },
    "jobtypes": "List <string>"
}
```
**Required keys :** 
* name 
* username
* age
* gender
<br>

Jobtypes is a list which can hold any of the following values :

|  Code     |     Jobtype   |
|-----------|---------------| 
|   WFM     |   Maids       |
|   WFC     |   Chefs       |
|   WFD     |   Drivers     |
|   WFE     |   Electricians|
|   WFP     |   Plumbers    |

<br>

**Response :** 
* returns id of user




### `GET /<usertype>/history/<userid>`
Find history

**Arguments :**
* **usertype :** can be either 'user' or 'worker'
* **userid :** id returned at the time of creation
                

**Response :**
* Returns a list of "placements" of the user/worker.
* Returns empty list if no history exists


________________________________
<br>
Common Response Codes :

* **200**: SUCCESS
* **400**: Bad Request
* **500**: Internal Server Error (or Application Error)

