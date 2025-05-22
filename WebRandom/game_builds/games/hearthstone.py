import random

# Список карт Hearthstone с путями, начинающимися с /static/
CARDS = [
    {"name": "Fireball", "class": "Mage", "rarity": "Common", "image": "images/hearthstone/fireball.png"},
    {"name": "Frostbolt", "class": "Mage", "rarity": "Common", "image": "images/hearthstone/frostbolt.png"},
    {"name": "Arcane Intellect", "class": "Mage", "rarity": "Common", "image": "images/hearthstone/arcane_intellect.png"},
    {"name": "Flamestrike", "class": "Mage", "rarity": "Common", "image": "images/hearthstone/flamestrike.png"},
    {"name": "Swipe", "class": "Druid", "rarity": "Common", "image": "images/hearthstone/swipe.png"},
    {"name": "Innervate", "class": "Druid", "rarity": "Rare", "image": "images/hearthstone/innervate.png"},
    {"name": "Consecration", "class": "Paladin", "rarity": "Common", "image": "images/hearthstone/consecration.png"},
    {"name": "Equality", "class": "Paladin", "rarity": "Rare", "image": "images/hearthstone/equality.png"},
    {"name": "Tirion Fordring", "class": "Paladin", "rarity": "Legendary", "image": "images/hearthstone/tirion_fordring.png"},
    {"name": "Bloodmage Thalnos", "class": "Neutral", "rarity": "Legendary", "image": "images/hearthstone/bloodmage_thalnos.png"},
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

    deck = random.sample(available_cards, min(30, len(available_cards)))

    return {
        "hero_class": hero_class or "Any",
        "deck": deck
    }