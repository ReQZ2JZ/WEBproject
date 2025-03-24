import os
import requests
from urllib.parse import quote
import time

def download_image(url, filepath):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {filepath}")
            return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
    return False

def create_directories():
    os.makedirs('static/images/heroes', exist_ok=True)
    os.makedirs('static/images/items', exist_ok=True)

def download_hero_images():
    heroes = [
        # Сила
        "Abaddon", "Alchemist", "Axe", "Beastmaster", "Brewmaster", "Bristleback", "Broodmother", "Centaur Warrunner", "Chaos Knight",
        "Clockwerk", "Dawnbreaker", "Doom", "Dragon Knight", "Earth Spirit", "Earthshaker", "Elder Titan",
        "Huskar", "Io", "Kunkka", "Legion Commander", "Lifestealer", "Lycan", "Magnus", "Marci",
        "Mars", "Night Stalker", "Omniknight", "Phoenix", "Primal Beast", "Pudge", "Sand King",
        "Slardar", "Snapfire", "Spirit Breaker", "Sven", "Tidehunter", "Timbersaw", "Tiny",
        "Treant Protector", "Tusk", "Underlord", "Undying", "Wraith King", "Dawnbreaker", "Marci",
        
        # Ловкость
        "Anti-Mage", "Arc Warden", "Bloodseeker", "Bounty Hunter", "Clinkz", "Crystal Maiden",
        "Drow Ranger", "Ember Spirit", "Faceless Void", "Gyrocopter", "Hoodwink", "Juggernaut",
        "Lone Druid", "Luna", "Medusa", "Meepo", "Mirana", "Monkey King", "Morphling", "Naga Siren",
        "Nyx Assassin", "Pangolier", "Phantom Assassin", "Phantom Lancer", "Razor", "Riki",
        "Shadow Fiend", "Slark", "Sniper", "Spectre", "Templar Assassin", "Terrorblade",
        "Troll Warlord", "Ursa", "Vengeful Spirit", "Venomancer", "Viper", "Weaver", "Muerta",
        
        # Интеллект
        "Ancient Apparition", "Bane", "Batrider", "Crystal Maiden", "Dark Seer", "Dark Willow", "Dazzle", "Death Prophet",
        "Disruptor", "Enchantress", "Enigma", "Grimstroke", "Invoker", "Jakiro", "Keeper of the Light",
        "Leshrac", "Lich", "Lina", "Lion", "Nature's Prophet", "Necrophos", "Oracle", "Outworld Destroyer",
        "Puck", "Queen of Pain", "Rubick", "Shadow Demon", "Shadow Shaman", "Silencer", "Skywrath Mage",
        "Storm Spirit", "Techies", "Tinker", "Visage", "Void Spirit", "Warlock", "Witch Doctor", "Zeus",
        "Hoodwink", "Dawnbreaker", "Marci", "Muerta"
    ]

    for hero in heroes:
        hero_name = hero.lower().replace(' ', '_')
        url = f"https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/{hero_name}.png"
        filepath = f"static/images/heroes/{hero_name}.png"
        download_image(url, filepath)
        time.sleep(0.5)  # Задержка между запросами

def download_item_images():
    items = {
        "Starting Items": [
            "Tango", "Healing Salve", "Clarity", "Faerie Fire", "Iron Branch", "Circlet",
            "Gauntlets of Strength", "Slippers of Agility", "Mantle of Intelligence", "Blight Stone",
            "Orb of Venom", "Quelling Blade", "Stout Shield", "Ring of Protection", "Magic Stick",
            "Enchanted Mango", "Observer Ward", "Sentry Ward", "Smoke of Deceit", "Town Portal Scroll",
            "Animal Courier", "Flying Courier", "Tome of Knowledge", "Dust of Appearance", "Gem of True Sight"
        ],
        "Early Game": [
            "Magic Wand", "Bracer", "Wraith Band", "Null Talisman", "Phase Boots", "Power Treads",
            "Arcane Boots", "Guardian Greaves", "Soul Ring", "Urn of Shadows", "Medallion of Courage",
            "Ring of Basilius", "Headdress", "Buckler", "Vladmir's Offering", "Boots of Speed",
            "Wind Lace", "Infused Raindrop", "Raindrops", "Bottle", "Hand of Midas", "Helm of Iron Will",
            "Chainmail", "Ring of Health", "Void Stone", "Energy Booster", "Point Booster", "Vitality Booster",
            "Boots of Travel", "Phase Boots", "Power Treads", "Arcane Boots", "Guardian Greaves",
            "Soul Ring", "Urn of Shadows", "Medallion of Courage", "Ring of Basilius", "Headdress",
            "Buckler", "Vladmir's Offering", "Wind Lace", "Infused Raindrop", "Raindrops", "Bottle"
        ],
        "Mid Game": [
            "Drum of Endurance", "Veil of Discord", "Eul's Scepter of Divinity", "Force Staff",
            "Blink Dagger", "Aether Lens", "Vanguard", "Hood of Defiance", "Pipe of Insight",
            "Glimmer Cape", "Ghost Scepter", "Rod of Atos", "Mekansm", "Guardian Greaves",
            "Crimson Guard", "Solar Crest", "Aeon Disk", "Lotus Orb", "Diffusal Blade",
            "Manta Style", "Sange", "Yasha", "Kaya", "Echo Sabre", "Mask of Madness",
            "Crystalys", "Armlet of Mordiggian", "Shadow Blade", "Dragon Lance",
            "Hurricane Pike", "Aghanim's Scepter", "Aghanim's Shard", "Eul's Scepter",
            "Force Boots", "Spirit Vessel", "Vladmir's Offering", "Helm of the Dominator",
            "Holy Locket", "Pavise", "Wraith Pact", "Eternal Shroud", "Mage Slayer",
            "Overwhelming Blink", "Swift Blink", "Arcane Blink", "Revenant's Brooch",
            "Drum of Endurance", "Veil of Discord", "Force Staff", "Blink Dagger", "Aether Lens",
            "Vanguard", "Hood of Defiance", "Pipe of Insight", "Glimmer Cape", "Ghost Scepter",
            "Rod of Atos", "Mekansm", "Crimson Guard", "Solar Crest", "Aeon Disk", "Lotus Orb"
        ],
        "Late Game": [
            "Abyssal Blade", "Assault Cuirass", "Battle Fury", "Black King Bar", "Bloodthorn",
            "Butterfly", "Daedalus", "Desolator", "Divine Rapier", "Eye of Skadi", "Heart of Tarrasque",
            "Linken's Sphere", "Manta Style", "Monkey King Bar", "Nullifier", "Octarine Core",
            "Radiance", "Refresher Orb", "Satanic", "Scythe of Vyse", "Shiva's Guard",
            "Skull Basher", "Sphere", "Travel Boots", "Vladmir's Offering", "Bloodstone",
            "Ethereal Blade", "Hand of Midas", "Mjollnir", "MKB", "Rapier", "Silver Edge",
            "Assault Cuirass", "Butterfly", "Daedalus", "Divine Rapier", "Eye of Skadi",
            "Heart of Tarrasque", "Linken's Sphere", "Manta Style", "Monkey King Bar",
            "Nullifier", "Octarine Core", "Radiance", "Refresher Orb", "Satanic",
            "Scythe of Vyse", "Shiva's Guard", "Skull Basher", "Sphere", "Travel Boots",
            "Abyssal Blade", "Battle Fury", "Black King Bar", "Bloodthorn", "Desolator",
            "Divine Rapier", "Eye of Skadi", "Heart of Tarrasque", "Linken's Sphere",
            "Monkey King Bar", "Nullifier", "Octarine Core", "Radiance", "Refresher Orb",
            "Satanic", "Scythe of Vyse", "Shiva's Guard", "Skull Basher", "Sphere",
            "Travel Boots", "Bloodstone", "Ethereal Blade", "Mjollnir", "Silver Edge"
        ]
    }

    for category in items.values():
        for item in category:
            item_name = item.lower().replace(' ', '_').replace('\'', '')
            url = f"https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/items/{item_name}.png"
            filepath = f"static/images/items/{item_name}.png"
            download_image(url, filepath)
            time.sleep(0.5)  # Задержка между запросами

if __name__ == "__main__":
    create_directories()
    print("Downloading hero images...")
    download_hero_images()
    print("Downloading item images...")
    download_item_images()
    print("Done!") 