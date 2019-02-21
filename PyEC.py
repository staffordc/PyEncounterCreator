monsters = {
    "goblin": ["XP 50", "AC 15", "HP 7 (2d6)", "Speed 30 ft", "pg# 166"],
    "aarakocra": ["XP 50", "AC 12", "HP 13 (3d8)", "Speed 20ft, fly 50 ft", "pg# 12"],
    "ankheg": ["XP 450", "AC 14, 11 while prone", "HP 39 (6d10+6", "Speed 30 ft, burrow 10ft", "pg# 21"],
    "azer": ["XP 450", "AC 17", "HP 39 (6d8+12)", "Speed 30 ft", "pg# 22"],
    "banshee": ["XP 1,100", "AC 12", "HP 58 (13d8)", "Speed 0ft, fly 40 ft", "pg# 23"],
    "basilisk": ["XP 700", "AC 15", "HP 52 (8d8 + 16), Speed 20 ft", "pg#24"],
    "spectator": ["XP 700", "AC 14", "HP 39 (6d8 + 12)", "Speed 0 ft, fly 30 ft", "pg# 30"],
    "zombie": ["XP 50", "AC 8", "HP 22 (3d8)", "Speed 20 ft", "pg# 315"],
    "gnoll": ["XP 100", "AC 15", "HP 22 (5d8)", "Speed 30 ft", "pg# 163"],
}
for key, value in monsters.items():
    if ("XP 50" in value):
        print(key, value)
