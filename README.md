# Flask Server

## Getting Started

Clone the repository to your local system

### Setting up an environment

Create a new environment
```
py -m venv new_env
```

Activate it
```
new_env\Scripts\activate
```

### Installing the dependencies 

After cloning, install all packages from '''requirement.txt'''
```
pip install -r requirements.txt
```

Download Visual C++ from this <a href=http://go.microsoft.com/fwlink/?LinkId=691126&fixForIE=.exe>link</a>
Visual Studio is required in order to install python-bsonjs
```
pipenv install python-bsonjs
```

## Start Server


```
flask run
```

## List of APIs

### Create User

target - /create/user  
method - POST
json schema
{
    "name":"Sherlock Holmes",
    "email":"sherlocked@locked.in",
    "address": {
        "line1":"221-B",
        "line2":"Baker Street",
        "locality":"Baker?",
        "City":"London",
        "State":"UK",
        "pin":"sher"
    },
}

### Create Worker

target - /create/worker  
method - POST
json schema




