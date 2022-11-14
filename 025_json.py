import json

jsonString = '{"name":"awan", "gender":"male"}'
jsonConvert = json.loads(jsonString)

print(jsonConvert)
print(jsonConvert["name"])

jsonObject = {
    "name": "awan",
    "gender": "male",
    "age": [
        {"value": 27, "description": "Dua puluh tujuh"}
    ]
}

jsonVar = json.dumps(jsonObject, indent=1, sort_keys=True)
print(jsonVar)