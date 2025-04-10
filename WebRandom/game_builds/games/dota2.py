import random

def format_item_filename(item):
    # Приводит имя к нижнему регистру, заменяет пробелы на подчёркивания и удаляет апострофы
    return item.lower().replace(' ', '_').replace("'", "")

def generate_dota2_build():
    heroes = [
        "Abaddon", "Alchemist", "Axe", "Beastmaster", "Brewmaster", "Bristleback", "Broodmother", 
        "Centaur Warrunner", "Chaos Knight", "Clockwerk", "Dawnbreaker", "Doom", "Dragon Knight", 
        "Earth Spirit", "Earthshaker", "Elder Titan", "Huskar", "Io", "Kunkka", "Legion Commander", 
        "Lifestealer", "Lycan", "Magnus", "Marci", "Mars", "Night Stalker", "Omniknight", "Phoenix", 
        "Primal Beast", "Pudge", "Sand King", "Slardar", "Snapfire", "Spirit Breaker", "Sven", 
        "Tidehunter", "Timbersaw", "Tiny", "Treant Protector", "Tusk", "Underlord", "Undying", "Wraith King",
        "Anti-Mage", "Arc Warden", "Bloodseeker", "Bounty Hunter", "Clinkz", "Crystal Maiden", 
        "Drow Ranger", "Ember Spirit", "Faceless Void", "Gyrocopter", "Hoodwink", "Juggernaut", 
        "Lone Druid", "Luna", "Medusa", "Meepo", "Mirana", "Monkey King", "Morphling", "Naga Siren", 
        "Nyx Assassin", "Pangolier", "Phantom Assassin", "Phantom Lancer", "Razor", "Riki", 
        "Shadow Fiend", "Slark", "Sniper", "Spectre", "Templar Assassin", "Terrorblade", 
        "Troll Warlord", "Ursa", "Vengeful Spirit", "Venomancer", "Viper", "Weaver",
        "Ancient Apparition", "Bane", "Batrider", "Crystal Maiden", "Dark Seer", "Dark Willow", 
        "Dazzle", "Death Prophet", "Disruptor", "Enchantress", "Enigma", "Grimstroke", "Invoker", 
        "Jakiro", "Keeper of the Light", "Leshrac", "Lich", "Lina", "Lion", "Nature's Prophet", 
        "Necrophos", "Oracle", "Outworld Destroyer", "Puck", "Queen of Pain", "Rubick", "Shadow Demon", 
        "Shadow Shaman", "Silencer", "Skywrath Mage", "Storm Spirit", "Techies", "Tinker", "Visage", 
        "Void Spirit", "Warlock", "Witch Doctor", "Zeus"
    ]

    items = {
        "Late Game": [
            "Abyssal Blade", "Assault Cuirass", "Battle Fury", "Black King Bar", "Bloodthorn",
            "Butterfly", "Daedalus", "Desolator", "Divine Rapier", "Eye of Skadi", "Heart of Tarrasque",
            "Linken's Sphere", "Manta Style", "Monkey King Bar", "Nullifier", "Octarine Core",
            "Radiance", "Refresher Orb", "Satanic", "Scythe of Vyse", "Shiva's Guard",
            "Skull Basher", "Sphere", "Travel Boots", "Vladmir's Offering"
        ]
    }

    # Выбираем случайного героя и формируем URL его изображения
    hero = random.choice(heroes)
    hero_image = f"/static/images/heroes/{format_item_filename(hero)}.png"

    # Выбираем 6 late game предметов
    late_items = [
        {
            "name": item, 
            "image_png": f"/static/images/items/{format_item_filename(item)}.png"
        } 
        for item in random.sample(items["Late Game"], 6)
    ]

    build = {
        "hero": hero,
        "hero_image_png": hero_image,
        "late_items": late_items,
    }
    return build
