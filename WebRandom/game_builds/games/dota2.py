import random

def format_item_filename(item):
    # Приводит имя к нижнему регистру, заменяет пробелы на подчёркивания и удаляет апострофы
    return item.lower().replace(' ', '_').replace("'", "")

def generate_dota2_build():
    heroes = [
        # Сила
        "Abaddon", "Alchemist", "Axe", "Beastmaster", "Brewmaster", "Bristleback", "Broodmother", 
        "Centaur Warrunner", "Chaos Knight", "Clockwerk", "Dawnbreaker", "Doom", "Dragon Knight", 
        "Earth Spirit", "Earthshaker", "Elder Titan", "Huskar", "Io", "Kunkka", "Legion Commander", 
        "Lifestealer", "Lycan", "Magnus", "Marci", "Mars", "Night Stalker", "Omniknight", "Phoenix", 
        "Primal Beast", "Pudge", "Sand King", "Slardar", "Snapfire", "Spirit Breaker", "Sven", 
        "Tidehunter", "Timbersaw", "Tiny", "Treant Protector", "Tusk", "Underlord", "Undying", "Wraith King",
        # Ловкость
        "Anti-Mage", "Arc Warden", "Bloodseeker", "Bounty Hunter", "Clinkz", "Crystal Maiden", 
        "Drow Ranger", "Ember Spirit", "Faceless Void", "Gyrocopter", "Hoodwink", "Juggernaut", 
        "Lone Druid", "Luna", "Medusa", "Meepo", "Mirana", "Monkey King", "Morphling", "Naga Siren", 
        "Nyx Assassin", "Pangolier", "Phantom Assassin", "Phantom Lancer", "Razor", "Riki", 
        "Shadow Fiend", "Slark", "Sniper", "Spectre", "Templar Assassin", "Terrorblade", 
        "Troll Warlord", "Ursa", "Vengeful Spirit", "Venomancer", "Viper", "Weaver",
        # Интеллект
        "Ancient Apparition", "Bane", "Batrider", "Crystal Maiden", "Dark Seer", "Dark Willow", 
        "Dazzle", "Death Prophet", "Disruptor", "Enchantress", "Enigma", "Grimstroke", "Invoker", 
        "Jakiro", "Keeper of the Light", "Leshrac", "Lich", "Lina", "Lion", "Nature's Prophet", 
        "Necrophos", "Oracle", "Outworld Destroyer", "Puck", "Queen of Pain", "Rubick", "Shadow Demon", 
        "Shadow Shaman", "Silencer", "Skywrath Mage", "Storm Spirit", "Techies", "Tinker", "Visage", 
        "Void Spirit", "Warlock", "Witch Doctor", "Zeus"
    ]
    
    items = {
        "Starting Items": [
            "Tango", "Healing Salve", "Clarity", "Faerie Fire", "Iron Branch", "Circlet",
            "Gauntlets of Strength", "Slippers of Agility", "Mantle of Intelligence", "Blight Stone",
            "Orb of Venom", "Quelling Blade", "Stout Shield", "Ring of Protection", "Magic Stick"
        ],
        "Early Game": [
            "Magic Wand", "Bracer", "Wraith Band", "Null Talisman", "Phase Boots", "Power Treads",
            "Arcane Boots", "Guardian Greaves", "Soul Ring", "Urn of Shadows", "Medallion of Courage",
            "Ring of Basilius", "Headdress", "Buckler", "Vladmir's Offering"
        ],
        "Mid Game": [
            "Drum of Endurance", "Veil of Discord", "Eul's Scepter of Divinity", "Force Staff",
            "Blink Dagger", "Aether Lens", "Vanguard", "Hood of Defiance", "Pipe of Insight",
            "Glimmer Cape", "Ghost Scepter", "Rod of Atos", "Mekansm", "Guardian Greaves",
            "Crimson Guard", "Solar Crest", "Aeon Disk", "Lotus Orb", "Diffusal Blade",
            "Manta Style", "Sange", "Yasha", "Kaya", "Echo Sabre", "Mask of Madness",
            "Crystalys", "Armlet of Mordiggian", "Shadow Blade", "Dragon Lance",
            "Hurricane Pike", "Aghanim's Scepter", "Aghanim's Shard"
        ],
        "Late Game": [
            "Abyssal Blade", "Assault Cuirass", "Battle Fury", "Black King Bar", "Bloodthorn",
            "Butterfly", "Daedalus", "Desolator", "Divine Rapier", "Eye of Skadi", "Heart of Tarrasque",
            "Linken's Sphere", "Manta Style", "Monkey King Bar", "Nullifier", "Octarine Core",
            "Radiance", "Refresher Orb", "Satanic", "Scythe of Vyse", "Shiva's Guard",
            "Skull Basher", "Sphere", "Travel Boots", "Vladmir's Offering"
        ]
    }
    
    # Выбираем случайного героя
    hero = random.choice(heroes)
    
    # Добавляем URL картинки героя, используя ту же функцию форматирования
    hero_image = f"/static/images/heroes/{format_item_filename(hero)}.png"
    
    starting_items = [{"name": item, "image_png": f"/static/images/items/{format_item_filename(item)}.png"} for item in random.sample(items["Starting Items"], 3)]
    early_items   = [{"name": item, "image_png": f"/static/images/items/{format_item_filename(item)}.png"} for item in random.sample(items["Early Game"], 2)]
    mid_items     = [{"name": item, "image_png": f"/static/images/items/{format_item_filename(item)}.png"} for item in random.sample(items["Mid Game"], 2)]
    late_items    = [{"name": item, "image_png": f"/static/images/items/{format_item_filename(item)}.png"} for item in random.sample(items["Late Game"], 2)]
    
    build = {
        "hero": hero,
        "hero_image_png": hero_image,
        "starting_items": starting_items,
        "early_game": early_items,
        "mid_game": mid_items,
        "late_game": late_items,
    }
    return build
