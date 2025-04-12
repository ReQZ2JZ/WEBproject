import os
import requests
import time

def download_image(url, filepath):
    if os.path.exists(filepath):
        print(f"Skipped: {filepath} already exists")
        return True
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {filepath}")
            return True
        else:
            print(f"Error downloading {url}: Status {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")
    return False

def create_directories():
    os.makedirs('static/images/heroes', exist_ok=True)
    os.makedirs('static/images/items', exist_ok=True)

def download_hero_images():
    # Список героев из твоего dota2.py
    heroes = [
        "Anti-Mage", "Faceless Void", "Juggernaut", "Terrorblade", "Spectre",
        "Phantom Assassin", "Riki", "Drow Ranger", "Medusa", "Morphling",
        "Luna", "Slark", "Sniper", "Ursa", "Troll Warlord", "Naga Siren",
        "Monkey King", "Chaos Knight", "Lifestealer", "Wraith King",
        "Shadow Fiend", "Templar Assassin", "Invoker", "Storm Spirit", "Queen of Pain",
        "Puck", "Tinker", "Ember Spirit", "Zeus", "Outworld Destroyer", "Huskar",
        "Death Prophet", "Leshrac", "Lina", "Dragon Knight", "Batrider", "Arc Warden",
        "Void Spirit", "Axe", "Mars", "Timbersaw", "Centaur Warrunner", "Underlord",
        "Doom", "Bristleback", "Slardar", "Tidehunter", "Night Stalker", "Sand King",
        "Beastmaster", "Pangolier", "Dark Seer", "Magnus", "Broodmother",
        "Primal Beast", "Abaddon", "Clockwerk", "Treant Protector", "Crystal Maiden",
        "Lich", "Witch Doctor", "Warlock", "Jakiro", "Disruptor", "Bane",
        "Shadow Shaman", "Lion", "Dazzle", "Omniknight", "Oracle", "Io",
        "Grimstroke", "Rubick", "Dark Willow", "Enchantress", "Chen", "Silencer",
        "Techies", "Keeper of the Light", "Ancient Apparition", "Skywrath Mage",
        "Shadow Demon", "Vengeful Spirit", "Snapfire", "Marci", "Tusk",
        "Earthshaker", "Earth Spirit", "Phoenix", "Bounty Hunter", "Pudge",
        "Nyx Assassin", "Meepo", "Mirana", "Clinkz", "Hoodwink", "Weaver",
        "Spirit Breaker", "Venomancer", "Nature's Prophet", "Enigma", "Visage",
        "Necrophos", "Alchemist", "Viper"
    ]

    # Получаем данные героев из API OpenDota
    response = requests.get("https://api.opendota.com/api/heroes")
    if response.status_code != 200:
        print(f"Failed to fetch heroes: {response.status_code}")
        return
    api_heroes = response.json()
    hero_dict = {hero['localized_name']: hero for hero in api_heroes}

    for hero in heroes:
        hero_name = hero.lower().replace(' ', '_').replace("'", "")
        filepath = f"static/images/heroes/{hero_name}.png"
        hero_data = hero_dict.get(hero)

        if not hero_data or 'img' not in hero_data or not hero_data['img']:
            print(f"Warning: No image for {hero}, trying Wiki")
            wiki_hero_name = hero.replace(' ', '_')
            wiki_url = f"https://static.wikia.nocookie.net/dota2_gamepedia/images/{wiki_hero_name[0].lower()}/{wiki_hero_name}_icon.png"
            if not download_image(wiki_url, filepath):
                placeholder_url = "https://via.placeholder.com/150"  # Новая заглушка
                download_image(placeholder_url, filepath)
            continue

        img_url = "https://api.opendota.com" + hero_data['img']
        if not download_image(img_url, filepath):
            wiki_hero_name = hero.replace(' ', '_')
            wiki_url = f"https://static.wikia.nocookie.net/dota2_gamepedia/images/{wiki_hero_name[0].lower()}/{wiki_hero_name}_icon.png"
            if not download_image(wiki_url, filepath):
                placeholder_url = "https://via.placeholder.com/150"  # Новая заглушка
                download_image(placeholder_url, filepath)
        time.sleep(0.2)

def download_item_images():
    # Список предметов из твоего dota2.py
    items = [
        "Abyssal Blade", "Assault Cuirass", "Battle Fury", "Black King Bar", "Bloodthorn",
        "Butterfly", "Daedalus", "Desolator", "Divine Rapier", "Eye of Skadi", "Heart of Tarrasque",
        "Linken's Sphere", "Manta Style", "Monkey King Bar", "Nullifier", "Octarine Core",
        "Radiance", "Refresher Orb", "Satanic", "Scythe of Vyse", "Shiva's Guard",
        "Skull Basher", "Sphere", "Travel Boots", "Vladmir's Offering"
    ]

    # Получаем данные предметов из API OpenDota
    response = requests.get("https://api.opendota.com/api/constants/items")
    if response.status_code != 200:
        print(f"Failed to fetch items: {response.status_code}")
        return
    api_items = response.json()

    # Маппинг для OpenDota
    item_mapping_opendota = {
        "Abyssal Blade": "abyssal_blade",
        "Assault Cuirass": "assault_cuirass",
        "Battle Fury": "bfury",
        "Black King Bar": "black_king_bar",
        "Bloodthorn": "bloodthorn",
        "Butterfly": "butterfly",
        "Daedalus": "daedalus",
        "Desolator": "desolator",
        "Divine Rapier": "rapier",
        "Eye of Skadi": "skadi",
        "Heart of Tarrasque": "heart",
        "Linken's Sphere": "linkens_sphere",
        "Manta Style": "manta_style",
        "Monkey King Bar": "monkey_king_bar",
        "Nullifier": "nullifier",
        "Octarine Core": "octarine_core",
        "Radiance": "radiance",
        "Refresher Orb": "refresher",
        "Satanic": "satanic",
        "Scythe of Vyse": "sheepstick",
        "Shiva's Guard": "shivas_guard",
        "Skull Basher": "basher",
        "Sphere": "linkens_sphere",
        "Travel Boots": "travel_boots",
        "Vladmir's Offering": "vladmirs_offering"  # Уже исправлено
    }

    # Маппинг для Steam CDN
    item_mapping_steam = {
        "Abyssal Blade": "abyssal_blade",
        "Assault Cuirass": "assault_cuirass",
        "Battle Fury": "bfury",
        "Black King Bar": "black_king_bar",
        "Bloodthorn": "bloodthorn",
        "Butterfly": "butterfly",
        "Daedalus": "daedalus",
        "Desolator": "desolator",
        "Divine Rapier": "rapier",
        "Eye of Skadi": "skadi",
        "Heart of Tarrasque": "heart",
        "Linken's Sphere": "linken_s_sphere",
        "Manta Style": "manta",
        "Monkey King Bar": "monkey_king_bar",
        "Nullifier": "nullifier",
        "Octarine Core": "octarine_core",
        "Radiance": "radiance",
        "Refresher Orb": "refresher",
        "Satanic": "satanic",
        "Scythe of Vyse": "sheepstick",
        "Shiva's Guard": "shivas_guard",
        "Skull Basher": "basher",
        "Sphere": "linken_s_sphere",
        "Travel Boots": "travel_boots",
        "Vladmir's Offering": "vladmir"
    }

    for item in items:
        # Имя для сохранения файла
        item_filename = item.lower().replace(' ', '_').replace("'", "")
        filepath = f"static/images/items/{item_filename}.png"

        # 1. Пробуем OpenDota
        item_key = item_mapping_opendota.get(item, item.lower().replace(' ', '_').replace("'", ""))
        found_item = None
        for key, item_data in api_items.items():
            if item_data.get('dname', '').lower().replace(' ', '_') == item_key:
                found_item = item_data
                break

        if found_item and 'img' in found_item and found_item['img']:
            img_url = "https://api.opendota.com" + found_item['img']
            if download_image(img_url, filepath):
                continue

        # 2. Пробуем Steam CDN
        print(f"Warning: No image for {item} on OpenDota, trying Steam CDN")
        steam_item_name = item_mapping_steam.get(item, item.lower().replace(' ', '_').replace("'", ""))
        steam_url = f"https://cdn.dota2.com/apps/dota2/images/items/{steam_item_name}_lg.png"
        if download_image(steam_url, filepath):
            continue

        # 3. Заглушка
        print(f"Warning: No image for {item} on Steam CDN, using placeholder")
        placeholder_url = "https://via.placeholder.com/150"  # Новая заглушка
        download_image(placeholder_url, filepath)
        time.sleep(0.2)

if __name__ == "__main__":
    create_directories()
    print("Downloading hero images...")
    download_hero_images()
    print("Downloading item images...")
    download_item_images()
    print("Done!")