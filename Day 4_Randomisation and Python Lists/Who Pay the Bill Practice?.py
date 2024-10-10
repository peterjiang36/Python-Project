import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# use random.choice() to randomly choose from a list
print(random.choice(friends) + " will pay for the bill!")

# use random.randint() to randomly generate the index of the list
who_will_pay = random.randint(0,4)
print(f"{friends[who_will_pay]} will pay for the bill!")