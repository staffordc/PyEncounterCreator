import pprint
import time

pp = pprint.PrettyPrinter(indent=0, width=160)

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

players = int(input(
    "How many players are you creating an encounter for? (Please use 1, 2, 3, etc.): "))
players_str = str(players)
print("Party of "+players_str+" your encounter is underway!")
time.sleep(1)
player_size = []
for x in range(players):
    player_size.append(input("What level is player : "))

print(player_size)


def player_input_experience(intput, dictionary):
    new_dictionary = {}
    for key, value in dictionary.items():
        if(intput in value and intput == value[0] or intput > value[0]):
            new_dictionary[key] = value
    return new_dictionary


difficulty = input(
    "How difficult is this encounter? (e)asy, (m)edium, (h)ard, (d)eadly? : ")
difficulty = difficulty.upper()
if difficulty == 'E':
    print("Alright, take it easy on em, sure.")
    for i, x in enumerate(player_size):
        if x == '1':
            player_size[i] = 25
        elif x == '2':
            player_size[i] = 50
        elif x == '3':
            player_size[i] = 75
        elif x == '4':
            player_size[i] = 100
    print(player_size)
    xp_sum = sum(player_size)
    print(xp_sum)
elif difficulty == 'M':
    print("Okay, so a fair fight")
    for i, x in enumerate(player_size):
        if x == '1':
            player_size[i] = 50
        if x == '2':
            player_size[i] = 100
        if x == '3':
            player_size[i] = 150
        if x == '4':
            player_size[i] = 200
    print(player_size)
    xp_sum = sum(player_size)
    print(xp_sum)
elif difficulty == 'H':
    print("So you want to see them struggle, and maybe lose someone?")
    for i, x in enumerate(player_size):
        if x == '1':
            player_size[i] = 75
        if x == '2':
            player_size[i] = 150
        if x == '3':
            player_size[i] = 225
        if x == '4':
            player_size[i] = 400
    print(player_size)
    xp_sum = sum(player_size)
    print(xp_sum)
elif difficulty == 'D':
    print("This is how you get a party wipe, dude.")
    for i, x in enumerate(player_size):
        if x == '1':
            player_size[i] = 125
        if x == '2':
            player_size[i] = 250
        if x == '3':
            player_size[i] = 375
        if x == '4':
            player_size[i] = 500
    print(player_size)
    xp_sum = sum(player_size)
else:
    print("You need to type e, m, h, or d for difficulty")


def horde_makeup_same(exp_input, dictionary):
    monster_name = input(
        "What is the name of the monster you want? ")
    for key, value in dictionary.items():
        if (key in dictionary):
            base_exp = value[0]
            ###print("base_exp: " + base_exp)
            experience_maths(base_exp, exp_input, monster_name, dictionary)
        else:
            print("Please type your response again")
            return horde_makeup_same(exp_input, dictionary)


def horde_makeup(experience, dictionary):
    player_input = input(
        "Would you like help with challenge rating math? ")
    player_input_horde = player_input.lower()
    if(player_input_horde == 'y'):
        return horde_makeup_same(experience, dictionary)
    elif(player_input_horde == 'n'):
        pp.pprint(player_input_experience(experience, dictionary))        
    else:
        input("Sorry, didn't catch that, could you try again? ")
        horde_makeup(experience, dictionary)

            
            
def experience_maths(base_exp, exp_input, monster_name, dictionary):
    multi_monster = input("Would you like many of the same monster? (y or n) ")
    multi_monster = multi_monster.lower()
    challenge_rating = exp_input/base_exp
    ###print("challenge rating: " + challenge_rating)
    if(multi_monster == "y"):
        if(challenge_rating < 2 and challenge_rating >= 1.5):
            return"2 " + monster_name
        elif(challenge_rating >= 2 and challenge_rating < 2.5):
            return"6 " + monster_name
        elif(challenge_rating >= 2.5 and challenge_rating < 3):
            return"10 " + monster_name
        elif(challenge_rating >= 3 and challenge_rating < 4):
            return"14 " + monster_name
        elif(challenge_rating > 4):
            return"20 " + monster_name
        else:
            return "1 " + monster_name
    elif(multi_monster == "n"):
        print("I didn't actually figure this part out")
    else:
        print("Sorry, I didn't catch that, come again? ")
        experience_maths(base_exp, exp_input, monster_name, dictionary)
###pp.pprint(player_input_experience(experience, monsters))

###player_monster_list = (player_input_experience_experience(experience, monsters))

###same_horde_output = horde_makeup(experience, player_monster_list)

# print(same_horde_output)
