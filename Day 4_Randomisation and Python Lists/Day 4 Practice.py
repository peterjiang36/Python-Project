# import my_module
# import random
#
# # random_integer = random.randint(1,10)
# # print(random_integer)
# # print(my_module.my_favourite_number)
#
# # # 1 inclusively to 10 exclusively
# # random_number_0_to_1 = random.random() * 10
# # # print(random_number_0_to_1)
# #
# # # 1 to 10 inclusively
# # random_float = random.uniform(1, 10)
# # print(random_float)
#
# random_heads_or_tails = random.randint(0,1)
# if random_heads_or_tails == 0:
#     print("Head")
# else:
#     print("Tail")

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
states_of_america[1] = "Pencilvania"
states_of_america.append("Angelaland")
states_of_america.extend(["PeterLand", "LingLand"])
print(states_of_america)
states_of_america.insert(0, "TestLand")
print(states_of_america)
