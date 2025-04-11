import os
from django.core.management.base import BaseCommand
from game_builds.models import Game, Item
from django.conf import settings

class Command(BaseCommand):
    help = 'Загружает предметы League of Legends из папки media/game_images/item_images'

    def handle(self, *args, **options):
        try:
            game = Game.objects.get(slug="league-of-legends")
        except Game.DoesNotExist:
            self.stdout.write(self.style.ERROR("Игра League of Legends не найдена"))
            return

        item_dir = os.path.join(settings.MEDIA_ROOT, 'game_images', 'item_images')
        if not os.path.exists(item_dir):
            self.stdout.write(self.style.ERROR(f"Папка {item_dir} не найдена!"))
            return

        item_files = [f for f in os.listdir(item_dir) if f.lower().endswith(('.png', '.jpg'))]

        item_names_map = {
            "Infinity_Edge": "Infinity Edge",
            "Rabadons_Deathcap": "Rabadon's Deathcap",
            "Thornmail": "Thornmail",
            "Sunfire_Cape": "Sunfire Cape",
            "Phantom_Dancer": "Phantom Dancer",
            # Добавьте остальные предметы по необходимости
        }

        created = 0
        for filename in item_files:
            name_without_ext = os.path.splitext(filename)[0]
            readable_name = item_names_map.get(name_without_ext, name_without_ext.replace('_', ' '))
            if not Item.objects.filter(game=game, name=readable_name).exists():
                item = Item(
                    game=game,
                    name=readable_name,
                    category="Mid Game",
                    image=os.path.join('game_images', 'item_images', filename)
                )
                item.save()
                created += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Загружено {created} предметов в League of Legends"))
