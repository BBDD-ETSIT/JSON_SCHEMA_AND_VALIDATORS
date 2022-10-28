import json
import jsonschema
from jsonschema import validate


def get_schema():
    """This function loads the given schema available"""
    with open('example.schema.json', 'r') as file:
        schema = json.load(file)
    return schema


def validate_json(json_data):
    """REF: https://json-schema.org/ """
    # Describe what kind of json you expect.
    execute_api_schema = get_schema()

    try:
        validate(instance=json_data, schema=execute_api_schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        err = "Given JSON data is InValid"
        return False, err

    message = "Given JSON data is Valid"
    return True, message


# Convert json to python object.
# jsonData = json.loads('{"id" : "10","name": "DonOfDen","price":"12"}')
with open('example.json', 'r') as file:
        jsonData = json.load(file)

# validate it
is_valid, msg = validate_json(jsonData)
print(msg)