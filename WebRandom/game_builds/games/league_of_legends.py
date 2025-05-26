import random

def generate_league_of_legends_build():
    def format_image_name(name):
        return name.replace(" ", "").replace("'", "") + ".png"

    champions = [ "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion Sol",
        "Azir", "Bard", "Bel'Veth", "Blitzcrank", "Brand", "Braum", "Briar", "Caitlyn", "Camille", "Cassiopeia", 
        "Cho'Gath", "Corki", "Darius", "Diana", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", 
        "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", 
        "Hwei", "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx", "K'Sante", "Kai'Sa", 
        "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled", 
        "Kog'Maw", "LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", 
        "Maokai", "Master Yi", "Milio", "Miss Fortune", "Mordekaiser", "Morgana", "Naafiri", "Nami", "Nasus", "Nautilus", 
        "Neeko", "Nidalee", "Nilah", "Nocturne", "Nunu & Willump", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", 
        "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "Rek'Sai", "Rell", "Renata Glasc", "Renekton", "Rengar", "Riven", 
        "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed", 
        "Sion", "Sivir", "Skarner", "Smolder", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench", "Taliyah", 
        "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch", "Udyr", 
        "Urgot", "Varus", "Vayne", "Veigar", "Vel'Koz", "Vex", "Vi", "Viego", "Viktor", "Vladimir", "Volibear", 
        "Warwick", "Wukong", "Xayah", "Xerath", "Xin Zhao", "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed", "Zeri", 
        "Ziggs", "Zilean", "Zoe", "Zyra"
    ]

    mythic_items = [
        "Kraken Slayer", "Galeforce", "Immortal Shieldbow", "Goredrinker", "Stridebreaker",
        "Divine Sunderer", "Eclipse", "Duskblade of Draktharr", "Prowler's Claw",
        "Luden's Tempest", "Liandry's Anguish", "Everfrost", "Crown of the Shattered Queen",
        "Moonstone Renewer", "Shurelya's Battlesong", "Radiant Virtue"
    ]

    legendary_items = [
        "Infinity Edge", "The Collector", "Essence Reaver", "Lord Dominik's Regards",
        "Phantom Dancer", "Mortal Reminder", "Bloodthirster", "Runaan's Hurricane",
        "Black Cleaver", "Ravenous Hydra", "Sterak's Gage", "Death's Dance", "Serylda's Grudge",
        "Manamune", "Seraph's Embrace", "Zhonya's Hourglass", "Rabadon's Deathcap",
        "Void Staff", "Morellonomicon", "Shadowflame", "Cosmic Drive", "Nashor's Tooth",
        "Lich Bane", "Demonic Embrace", "Spirit Visage", "Thornmail", "Randuin's Omen",
        "Sunfire Aegis", "Force of Nature", "Frozen Heart", "Abyssal Mask", "Titanic Hydra"
    ]

    boots = [
        "Plated Steelcaps", "Mercury's Treads", "Berserker's Greaves",
        "Sorcerer's Shoes", "Mobility Boots", "Ionian Boots of Lucidity"
    ]

    unique_items = [
        "Guardian Angel", "Edge of Night", "Maw of Malmortius", "Banshee's Veil",
        "Silvermere Dawn", "Chempunk Chainsword", "Knight's Vow", "Zeke's Convergence"
    ]

    # 1 предмет из каждой категории
    mythic = random.choice(mythic_items)
    legendary = random.choice([item for item in legendary_items if item != mythic])
    boots_item = random.choice([item for item in boots if item not in [mythic, legendary]])
    unique = random.choice([item for item in unique_items if item not in [mythic, legendary, boots_item]])

    used = {mythic, legendary, boots_item, unique}
    remaining_pool = [item for item in (mythic_items + legendary_items + boots + unique_items) if item not in used]
    extra_items = random.sample(remaining_pool, 2)

    items = [mythic, legendary, boots_item, unique] + extra_items
    categories = ['Mythic', 'Legendary', 'Boots', 'Unique', 'Extra', 'Extra']

    champion = random.choice(champions)

    return {
    "champion": {
        "name": champion,
        "image": f"/static/images/League_of_Legends/champion_images/{format_image_name(champion)}"
    },
    "items": [
        {
            "name": item,
            "image": f"/static/images/League_of_Legends/item_images/{format_image_name(item)}",
            "category": categories[i]
        }
        for i, item in enumerate(items)
    ]
}

