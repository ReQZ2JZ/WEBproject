import random
from django.shortcuts import render
from django.http import JsonResponse

def format_item_filename(item):
    return item.lower().replace(' ', '_').replace("'", "")

heroes_by_role = {
    "carry": [
        "Anti-Mage", "Faceless Void", "Juggernaut", "Terrorblade", "Spectre",
        "Phantom Assassin", "Riki", "Drow Ranger", "Medusa", "Morphling",
        "Luna", "Slark", "Sniper", "Ursa", "Troll Warlord", "Naga Siren",
        "Monkey King", "Chaos Knight", "Lifestealer", "Wraith King"
    ],
    "offlane": [
        "Axe", "Mars", "Timbersaw", "Centaur Warrunner", "Underlord", "Doom",
        "Bristleback", "Slardar", "Tidehunter", "Night Stalker", "Sand King",
        "Beastmaster", "Pangolier", "Dark Seer", "Magnus", "Broodmother",
        "Primal Beast", "Abaddon", "Clockwerk", "Treant Protector"
    ],
    "support": [
        "Crystal Maiden", "Lich", "Witch Doctor", "Warlock", "Jakiro", "Disruptor",
        "Bane", "Shadow Shaman", "Lion", "Dazzle", "Omniknight", "Oracle", "Io",
        "Grimstroke", "Rubick", "Dark Willow", "Enchantress", "Chen", "Silencer",
        "Techies", "Keeper of the Light", "Ancient Apparition", "Skywrath Mage",
        "Shadow Demon", "Vengeful Spirit"
    ]
}

late_game_items = [
    "Abyssal Blade", "Assault Cuirass", "Battle Fury", "Black King Bar", "Bloodthorn",
    "Butterfly", "Daedalus", "Desolator", "Divine Rapier", "Eye of Skadi", "Heart of Tarrasque",
    "Manta Style", "Monkey King Bar", "Nullifier", "Octarine Core",
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
            "image_png": f"/static/images/items/{format_item_filename(item)}.png",
        }
        for item in random.sample(late_game_items, 6)
    ]

    return {
        "hero": hero,
        "hero_image_png": hero_image,
        "late_items": items,
        "role": role or "Случайная"
    }

def game_detail(request, slug):
    role = request.GET.get("role")
    build = generate_dota2_build(role)
    game = {"name": "Dota 2"}
    return render(request, 'game_builds/random_build.html', {'game': game, 'build': build})

def generate_build(request, slug):
    role = request.GET.get("role")
    print(f"Получен запрос для роли: {role}")  # Отладочный вывод
    build = generate_dota2_build(role)
    return JsonResponse(build)