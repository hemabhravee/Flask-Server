# Flask Server

## Getting Started

Clone the repository to your local system. Everything will be done inside this directory.

### Setting up an environment

Create a new environment
```
py -m venv new_env
```
This will create a folder new_env. <br>

Activate it
```
new_env\Scripts\activate
```

### Installing the dependencies 

After cloning, install all packages from ```requirements.txt```
```
pip install -r requirements.txt
```

Download Visual C++ from [here](http://go.microsoft.com/fwlink/?LinkId=691126&fixForIE=.exe) and install it.<br>
Visual Studio is required in order to install python-bsonjs.
```
pipenv install python-bsonjs
```

## Start Server

```
flask run
```

### [API Documentation](https://github.com/Wander-Force/Flask-Server/blob/master/apiDoc.md)
