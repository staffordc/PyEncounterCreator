import pprint
import time

pp = pprint.PrettyPrinter(indent=0)

monsters = {
    "goblin": [50, "AC 15", "HP 7 (2d6)", "Speed 30 ft", "pg# 166"],
    "aarakocra": [50, "AC 12", "HP 13 (3d8)", "Speed 20ft, fly 50 ft", "pg# 12"],
    "ankheg": [450, "AC 14, 11 prone", "HP 39 (6d10+6", "Speed 30 ft, burrow 10ft", "pg# 21"],
    "azer": [450, "AC 17", "HP 39 (6d8+12)", "Speed 30 ft", "pg# 22"],
    "banshee": [1100, "AC 12", "HP 58 (13d8)", "Speed 0ft, fly 40 ft", "pg# 23"],
    "basilisk": [700, "AC 15", "HP 52 (8d8 + 16), Speed 20 ft", "pg#24"],
    "spectator": [700, "AC 14", "HP 39 (6d8 + 12)", "Speed 0 ft, fly 30 ft", "pg# 30"],
    "needle blight": [50, "AC 12", "HP 11 (2d8 + 2)", "Speed 30 ft", "pg# 32"],
    "twig blight": [25, "AC 13", "HP 4 (1d6 + 1", "Speed 20 ft", "pg# 32"],
    "vine blight": [100, "AC 12", "HP 26 (4d8 + 8", "Speed 10 ft", "pg# 32"],
    "bugbear": [200, "AC 16", "HP 27 (5d8 + 5", "Speed 30 ft", "pg# 33"],
    "bugbear chief": [700, "AC 17", "HP 65 (10d8 + 20)", "Speed 30 ft", "pg# 33"],
    "bulette": [1800, "AC 17", "HP 94 (9d10 + 45", "Speed 40ft, burrow 40 ft", "pg#34"],
    "bullywug": [50, "AC 15", "HP 11 (2d8 + 2)", "Speed 20 ft, swim 40ft", "pg#35"],
    "cambion": [1800, "AC 19", "HP 82 (11d8 + 33", "Speed 30 ft, fly 60 ft", "pg#36"],
    "carrion crawler": [450, "AC 13", "HP 51 (6d10 + 18)", "Speed 30 ft, climb 30 ft", "pg#37"],
    "centaur": [450, "AC 12", "HP 45 (6d10 + 12)", "Speed 50 ft", "pg#38"],
    "chuul": [1100, "AC 16", "HP 93 (11d10 + 33", "Speed 30 ft, swim 30ft", "pg#40"],
    "cockatrice": [100, "AC 11", "HP 27 (6d6 + 6", "Speed 20ft, fly 40 ft", "pg#42"],
    "couatl": [1100, "AC 19", "HP 97 (13d8 + 39)", "Speed 30ft, fly 90 ft", "pg#43"],
    "crawling claw": [10, "AC 12", "HP 2 (1d4)", "Speed 20 ft, climb 20ft", "pg#44"],
    "darkmantle": [100, "AC 11", "HP 22 (5d6 + 5)", "Speed 10 ft, fly 30 ft", "pg#46"],
    "zombie": [50, "AC 8", "HP 22 (3d8)", "Speed 20 ft", "pg# 315"],
    "gnoll": [100, "AC 15", "HP 22 (5d8)", "Speed 30 ft", "pg# 163"],
}

players = int(input("How many players are you creating an encounter for? (Please use 1, 2, 3, etc.): "))
players_str = str(players)
print("Party of "+players_str+" your encounter is underway!")
time.sleep(1)
player_size = []
for x in range(players):
    player_size.append(input("What level is player : "))

print(player_size)
player_size_int = list(map(int, player_size))
print(player_size_int)

difficulty = input("How difficult is this encounter? (e)asy, (m)edium, (h)ard, (d)eadly? : ")
difficulty = difficulty.upper()
if difficulty == 'E':
    print("Alright, take it easy on em, sure.")
    for i, x in enumerate(player_size_int):
        player_size_int[i] = x * 25
    print(player_size_int)
    xp_sum = sum(player_size_int)
    print(xp_sum)
elif difficulty == 'M':
    print("Okay, so a fair fight")
    for i, x in enumerate(player_size_int):
        player_size_int[i] = x * 50
    print(player_size_int)
    xp_sum = sum(player_size_int)
    print(xp_sum)
elif difficulty == 'H':
    print("So you want to see them struggle, and maybe lose someone?")
    for i, x in enumerate(player_size_int):
        if x == 4:
            player_size_int[i] = 400
        else:
            player_size_int[i] = x * 75
    print(player_size_int)
    xp_sum = sum(player_size_int)
    print(xp_sum)
elif difficulty == 'D':
    print("This is how you get a party wipe, dude.")
    for i, x in enumerate(player_size_int):
        player_size_int[i] = x * 125
    print(player_size_int)
    xp_sum = sum(player_size_int)
else:
    print("You need to type e, m, h, or d for difficulty")

#pp.pprint(player_input_math(player_input, monsters))
