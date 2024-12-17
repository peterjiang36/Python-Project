# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected",
#     "Function": "A piece of code that you can easily call over and over again"
# }
#
# # print(programming_dictionary["Bug"])
#
# programming_dictionary["Loop"] = "The action of doint something over and over again."
# # print(programming_dictionary)
#
#
# # programming_dictionary = {}
# # print(programming_dictionary)
# programming_dictionary["Bug"] = "A moth in your computer"
# # print(programming_dictionary)
#
# # loop through a dictionary
#
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# nested list in dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }

# print(travel_log["France"][1])

# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])

travel_log = {
    "France": {
        "city_visited": ["Paris", "Lille", "Dijon"],
        "num_times_visited": 12
    },
    "Germany": {
        "city_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "num_times_visited": 5
    }
}
print(travel_log["Germany"]["city_visited"][2])