import random

def generate_world_of_tanks_build():
    tank_types = ["Тяжёлый танк", "Средний танк", "Лёгкий танк", "ПТ-САУ"]
    nations = ["СССР", "Германия", "США", "Великобритания", "Франция", "Япония", "Китай"]
    tiers = ["VIII", "IX", "X"]

    tanks = {
        "СССР": {
            "Тяжёлый танк": ["ИС-7", "Объект 277", "ИС-4"],
            "Средний танк": ["Объект 140", "Т-62А"],
            "Лёгкий танк": ["Т-100 ЛТ"],
            "ПТ-САУ": ["Объект 268"]
        }
    }

    tank_type = random.choice(tank_types)
    nation = random.choice(nations)

    while not tanks.get(nation, {}).get(tank_type):
        nation = random.choice(nations)

    return {
        "tank_type": tank_type,
        "nation": nation,
        "tank": random.choice(tanks[nation][tank_type]),
        "tier": random.choice(tiers)
    }
