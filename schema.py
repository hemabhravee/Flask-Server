userschema = {
    "type" : "object",
    "properties" : {
        "name" : {"type": "string"},
        "email" : {"type": "string"},
        "address" : {
            "type": "object",
            "properties" : {
                "line1" : {"type": "string"},
                "line2" : {"type": "string"},
                "locality" : {"type": "string"},
                "city" : {"type": "string"},
                "state" : {"type": "string"},
                "pin" : {"type": "string"},
            },
            "additionalProperties": False, 
        }
    },
    "required" : ["name", "email"],
    "additionalProperties": False,
}

workerschema = {
    "type" : "object",
    "properties" : {
        "name": {"type": "string"},
        "username": {"type": "string"},
        "age": {"type": "number"} ,
        "gender": {"type": "string"},
        "address": { 
            "type" : "object",
            "properties" : {
                "line1" : {"type": "string"},
                "line2" : {"type": "string"},
                "locality" : {"type": "string"},
                "city" : {"type": "string"},
                "state" : {"type": "string"},
                "pin" : {"type": "string"},
                },
            "additionalProperties": False,
            },
        "mobile" : {"type": "string"},
        "adhaar": {"type": "string"},
        "jobtypes":  {
            "type": "array",
            "items": {
                "type": "string"
            },
            "minItems": 1,
            "uniqueItems": True,
            
        }

    },
    "additionalProperties": False,
    "required" : ["name", "username", "age", "gender"]
    
}