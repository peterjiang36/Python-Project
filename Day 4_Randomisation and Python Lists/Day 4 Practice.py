import my_module
import random

# random_integer = random.randint(1,10)
# print(random_integer)
# print(my_module.my_favourite_number)

# # 1 inclusively to 10 exclusively
# random_number_0_to_1 = random.random() * 10
# # print(random_number_0_to_1)
#
# # 1 to 10 inclusively
# random_float = random.uniform(1, 10)
# print(random_float)

random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Head")
else:
    print("Tail")