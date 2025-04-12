import random

def generate_clash_royale_build():
    cards = [
        {"name": "Knight", "image": "/static/images/ClashRoyale/Knight.png", "rarity": "Common"},
        {"name": "Archers", "image": "/static/images/ClashRoyale/Archers.png", "rarity": "Common"},
        {"name": "Giant", "image": "/static/images/ClashRoyale/Giant.png", "rarity": "Rare"},
        {"name": "Baby Dragon", "image": "/static/images/ClashRoyale/BabyDragon.png", "rarity": "Epic"},
        {"name": "P.E.K.K.A", "image": "/static/images/ClashRoyale/PEKKA.png", "rarity": "Epic"},
        {"name": "Hog Rider", "image": "/static/images/ClashRoyale/HogRider.png", "rarity": "Rare"},
        {"name": "Fireball", "image": "/static/images/ClashRoyale/Fireball.png", "rarity": "Rare"},
        {"name": "Zap", "image": "/static/images/ClashRoyale/Zap.png", "rarity": "Common"},
        {"name": "Minions", "image": "/static/images/ClashRoyale/Minions.png", "rarity": "Common"},
        {"name": "Balloon", "image": "/static/images/ClashRoyale/Balloon.png", "rarity": "Epic"},
        {"name": "Wizard", "image": "/static/images/ClashRoyale/Wizard.png", "rarity": "Rare"},
        {"name": "The Log", "image": "/static/images/ClashRoyale/TheLog.png", "rarity": "Legendary"},
        {"name": "Goblin Barrel", "image": "/static/images/ClashRoyale/GoblinBarrel.png", "rarity": "Epic"},
        {"name": "Golden Knight", "image": "/static/images/ClashRoyale/GoldenKnight.png", "rarity": "Champion"},
        {"name": "Skeleton King", "image": "/static/images/ClashRoyale/SkeletonKing.png", "rarity": "Champion"},
        {"name": "Archer Queen", "image": "/static/images/ClashRoyale/ArcherQueen.png", "rarity": "Champion"}
    ]

    deck = random.sample(cards, 8)

    return {
        "deck": deck
    }