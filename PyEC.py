monsters = {
    "goblin": ["XP 50", "AC 15", "HP 7 (2d6)", "Speed 30 ft", "pg# 166"]
}
for key, value in monsters.items():
    if (key, value == "XP 50"):
        print(key, value)
