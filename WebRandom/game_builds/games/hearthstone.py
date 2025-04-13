import random

# Пример карт Hearthstone
CARDS = [
    {"name": "Fireball", "class": "Mage", "rarity": "Common", "image": "/static/images/hearthstone/fireball.png"},
    {"name": "Frostbolt", "class": "Mage", "rarity": "Common", "image": "/static/images/hearthstone/frostbolt.png"},
    {"name": "Arcane Intellect", "class": "Mage", "rarity": "Common", "image": "/static/images/hearthstone/arcane_intellect.png"},
    {"name": "Flamestrike", "class": "Mage", "rarity": "Common", "image": "/static/images/hearthstone/flamestrike.png"},
    {"name": "Swipe", "class": "Druid", "rarity": "Common", "image": "/static/images/hearthstone/swipe.png"},
    {"name": "Innervate", "class": "Druid", "rarity": "Rare", "image": "/static/images/hearthstone/innervate.png"},
    {"name": "Consecration", "class": "Paladin", "rarity": "Common", "image": "/static/images/hearthstone/consecration.png"},
    {"name": "Equality", "class": "Paladin", "rarity": "Rare", "image": "/static/images/hearthstone/equality.png"},
    {"name": "Tirion Fordring", "class": "Paladin", "rarity": "Legendary", "image": "/static/images/hearthstone/tirion_fordring.png"},
    {"name": "Bloodmage Thalnos", "class": "Neutral", "rarity": "Legendary", "image": "/static/images/hearthstone/bloodmage_thalnos.png"},
]

def generate_hearthstone_build(hero_class=None):
    """
    Генерирует случайную деку для указанного класса героя.
    Если класс не указан, выбираются карты из всех классов.
    """
    if hero_class:
        available_cards = [card for card in CARDS if card["class"] in [hero_class, "Neutral"]]
    else:
        available_cards = CARDS

    # Генерируем 30 случайных карт
    deck = random.sample(available_cards, min(30, len(available_cards)))

    return {
        "hero_class": hero_class or "Any",
        "deck": deck
    }