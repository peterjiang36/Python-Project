enemies = 1

def increase_enemies(enemy):

    print(f"enemies inside function: {enemies}")
    return enemy + 1


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")
#
# local scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
# drink_potion()
# print(potion_strength)

# # global scope
#
# player_health = 10
# def drink_potion():
#     potion_strength = 2
#     print(player_health)
# drink_potion()

# game_level = 10
# enemies = ["Skeleton", "Zombie", "Alien"]
# def create_enemy():
#     new_enemy = ""
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy)
# create_enemy()