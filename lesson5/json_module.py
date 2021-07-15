import json

# сериализация

# dict -> json
# list, tuple -> array
# str -> string
# int, float -> number
# True -> true
# False -> false
# None -> null

# dump() & dumps()
data = {"one": 1, "two": 2}

with open("my_file.json", "w") as f:
    json.dump(data, f)

json_str = json.dumps(data)
print(json_str)
print(type(json_str))

# десериализация
# load() & loads()

with open("test_json.json") as f:
    json_data = json.load(f)

print(json_data)
print(type(json_data))

dict_data = json.loads(json_str)
print(dict_data)
print(type(dict_data))
