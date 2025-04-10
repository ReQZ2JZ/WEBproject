import random

def generate_dead_by_daylight_build():
    roles = {
        "survivor": ["Дуайт", "Мегги", "Джей", "Клодета", "Нея"],
        "killer": ["Трапер", "Призрак", "Хилли Билли", "Медсестра", "Анна"]
    }

    # Случайно выбираем роль
    role = random.choice(list(roles.keys()))
    character = random.choice(roles[role])

    # Добавляем URL картинки персонажа
    character_image = f"/static/images/characters/{role}/{character}.png"

    perks = ["Borrowed Time", "Dead Hard", "Iron Will", "Sprint Burst"]
    items = ["Medkit", "Flashlight", "Toolbox", "Map"] if role == "survivor" else []

    build = {
        "role": role,
        "character": character,
        "character_image_png": character_image,
        "perks": random.sample(perks, 4),
        "item": random.choice(items) if items else None
    }

    return build