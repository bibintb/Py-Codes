import json
x = '{"name":"John", "age":30, "city":"New York"}' # json string
y = json.loads(x) # convert json string to python dict
print(y["age"]) # access python dict