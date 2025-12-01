print("--- 1. Basic Dictionary Operations ---")

player = {}

player['username'] = 'DragonSlayer'
player['level'] = 10
player['points'] = 50
print(f"Initial Player: {player}")

player['level'] = 11
print(f"Modified Level: {player['level']}")

del player['points']
print(f"Player after removing points: {player}")

print("\n--- 2. Accessing Data ---")

skill_ratings = {
    'archery': 85,
    'swordsmanship': 90,
    'stealth': 40,
    'magic': 75
}

print(f"Archery Skill: {skill_ratings['archery']}")

healing_skill = skill_ratings.get('healing', 'Skill not learned yet')
print(f"Healing Check: {healing_skill}")

print("\n--- 3. Looping Strategies ---")

print("All Skills and Ratings:")
for skill, rating in skill_ratings.items():
    print(f"- Key: {skill}, Value: {rating}")

print("\nList of available skills:")
for skill in skill_ratings.keys():
    print(f"- {skill.title()}")

print("\nSkills in alphabetical order:")
for skill in sorted(skill_ratings.keys()):
    print(f"- {skill.title()}")

print("\nJust the ratings:")
for rating in skill_ratings.values():
    print(rating)

print("\n--- 4. Nesting ---")

orc = {'type': 'orc', 'hp': 100}
goblin = {'type': 'goblin', 'hp': 50}
troll = {'type': 'troll', 'hp': 200}

enemies = [orc, goblin, troll]

print("A List of Dictionaries (First 2 enemies):")
for enemy in enemies[:2]:
    print(enemy)

quest_log = {
    'quest_name': 'Save the Kingdom',
    'rewards': ['Gold', 'Magic Sword', 'Honor'],
    'difficulty': 'Hard'
}

print(f"\nRewards for {quest_log['quest_name']}:")
for reward in quest_log['rewards']:
    print(f"\t- {reward}")

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

print("\nA Dictionary inside a Dictionary:")
for username, user_info in users.items():
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tUsername: {username}")
    print(f"\t\tFull name: {full_name.title()}")
    print(f"\t\tLocation: {location.title()}")