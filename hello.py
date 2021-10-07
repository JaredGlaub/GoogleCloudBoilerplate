import json

def hi():

    value = {
        "response1": "hi",
        "response2": "hello"
    }
    return json.dumps(value)
