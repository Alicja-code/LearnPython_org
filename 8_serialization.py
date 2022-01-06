import json
import pickle

# # takes an object and returns a String
# json_string = json.dumps([1, 2, 3, "a", "b", "c"])
# print(json_string)
#
# # load JSON back to a data structure
# print(json.loads(json_string))
#
# # Python proprietary data serialization method
# pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
# print(pickle.loads(pickled_string))


# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    # Add your code here
    # salaries_json from str to obj
    salaries_json_obj = json.loads(salaries_json)
    print(type(salaries_json_obj))
    salaries_json_obj[name] = salary
    # salaries_json from obj to str
    salaries_json = json.dumps(salaries_json_obj)
    print(type(salaries_json))
    return salaries_json


# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])
