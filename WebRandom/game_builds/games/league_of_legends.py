import random

def generate_league_of_legends_build():
    champions = ["Ahri", "Akali", "Ashe", "Darius", "Ezreal", "Garen", "Jinx", "Katarina", "Lux", "Yasuo"]
    items = ["Infinity Edge", "Rabadon's Deathcap", "Thornmail", "Sunfire Cape", "Phantom Dancer"]

    champion = random.choice(champions)
    build_items = random.sample(items, 3)

    return {
        "champion": champion,
        "items": build_items
    }