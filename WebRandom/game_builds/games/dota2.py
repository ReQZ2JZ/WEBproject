import random
from django.shortcuts import render

def format_item_filename(item):
    return item.lower().replace(' ', '_').replace("'", "")

heroes_by_role = {
    "Carry": [
        "Anti-Mage", "Faceless Void", "Juggernaut", "Terrorblade", "Spectre",
        "Phantom Assassin", "Riki", "Drow Ranger", "Medusa", "Morphling",
        "Luna", "Slark", "Sniper", "Ursa", "Troll Warlord", "Naga Siren",
        "Monkey King", "Chaos Knight", "Lifestealer", "Wraith King"
    ],
    "Midlaner": [
        "Shadow Fiend", "Templar Assassin", "Invoker", "Storm Spirit", "Queen of Pain",
        "Puck", "Tinker", "Ember Spirit", "Zeus", "Outworld Destroyer", "Huskar",
        "Death Prophet", "Leshrac", "Lina", "Dragon Knight", "Batrider", "Arc Warden",
        "Void Spirit"
    ],
    "Offlaner": [
        "Axe", "Mars", "Timbersaw", "Centaur Warrunner", "Underlord", "Doom",
        "Bristleback", "Slardar", "Tidehunter", "Night Stalker", "Sand King",
        "Beastmaster", "Pangolier", "Dark Seer", "Magnus", "Broodmother",
        "Primal Beast", "Abaddon", "Clockwerk", "Treant Protector"
    ],
    "Support": [
        "Crystal Maiden", "Lich", "Witch Doctor", "Warlock", "Jakiro", "Disruptor",
        "Bane", "Shadow Shaman", "Lion", "Dazzle", "Omniknight", "Oracle", "Io",
        "Grimstroke", "Rubick", "Dark Willow", "Enchantress", "Chen", "Silencer",
        "Techies", "Keeper of the Light", "Ancient Apparition", "Skywrath Mage",
        "Shadow Demon", "Vengeful Spirit"
    ],
    "Universal": [
        "Snapfire", "Marci", "Tusk", "Earthshaker", "Earth Spirit", "Phoenix",
        "Bounty Hunter", "Pudge", "Nyx Assassin", "Meepo", "Mirana", "Clinkz",
        "Hoodwink", "Weaver", "Spirit Breaker", "Venomancer", "Nature's Prophet",
        "Enigma", "Visage", "Necrophos", "Alchemist", "Leshrac", "Viper", "Lion",
        "Underlord", "Invoker"
    ]
}

late_game_items = [
    "Abyssal Blade", "Assault Cuirass", "Battle Fury", "Black King Bar", "Bloodthorn",
    "Butterfly", "Daedalus", "Desolator", "Divine Rapier", "Eye of Skadi", "Heart of Tarrasque",
    "Linken's Sphere", "Manta Style", "Monkey King Bar", "Nullifier", "Octarine Core",
    "Radiance", "Refresher Orb", "Satanic", "Scythe of Vyse", "Shiva's Guard",
    "Skull Basher", "Sphere", "Travel Boots", "Vladmir's Offering"
]

def generate_dota2_build(role=None):
    all_heroes = sum(heroes_by_role.values(), [])
    selected_pool = heroes_by_role.get(role, all_heroes)
    hero = random.choice(selected_pool)
    hero_image = f"/static/images/heroes/{format_item_filename(hero)}.png"

    items = [
        {
            "name": item,
            "image_png": f"/static/images/items/{format_item_filename(item)}.png"
        }
        for item in random.sample(late_game_items, 6)
    ]

    return {
        "hero": hero,
        "hero_image_png": hero_image,
        "late_items": items,
        "role": role or "Random"
    }

def game_detail(request, slug):
    role = request.GET.get("role")
    build = generate_dota2_build(role)
    game = {"name": "Dota 2"}
    return render(request, 'game_builds/random_build.html', {'game': game, 'build': build})
