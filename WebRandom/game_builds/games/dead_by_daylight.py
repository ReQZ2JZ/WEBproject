import random

def generate_dead_by_daylight_build():
    perks = ["Borrowed Time", "Dead Hard", "Iron Will", "Sprint Burst"]
    items = ["Medkit", "Flashlight", "Toolbox", "Map"]

    return {
        "perks": random.sample(perks, 4),
        "item": random.choice(items)
    }