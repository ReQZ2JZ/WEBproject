import os
import requests

CHAMPION_FOLDER = "media/champion_images"
ITEM_FOLDER = "media/item_images"
VERSION_URL = "https://ddragon.leagueoflegends.com/api/versions.json"
CDN_BASE = "https://ddragon.leagueoflegends.com/cdn"

# Функция нормализации имён
def normalize(name):
    return name.replace(" ", "").replace("'", "") + ".png"

# Получаем последнюю версию игры
def get_latest_version():
    try:
        versions = requests.get(VERSION_URL).json()
        return versions[0]
    except Exception as e:
        print("❌ Ошибка при получении версии:", e)
        return None

# Скачиваем изображения чемпионов
def download_champions(version):
    url = f"{CDN_BASE}/{version}/data/en_US/champion.json"
    try:
        champions = requests.get(url).json()["data"]
        os.makedirs(CHAMPION_FOLDER, exist_ok=True)

        for champ in champions.values():
            name = champ["id"]
            image_url = f"{CDN_BASE}/{version}/img/champion/{name}.png"
            file_path = os.path.join(CHAMPION_FOLDER, normalize(name))

            if not os.path.exists(file_path):
                r = requests.get(image_url)
                with open(file_path, "wb") as f:
                    f.write(r.content)
                print(f"✅ Champion: {name}")
            else:
                print(f"✔️ Champion already exists: {name}")
    except Exception as e:
        print("❌ Ошибка при скачивании чемпионов:", e)

# Скачиваем изображения предметов
def download_items(version):
    url = f"{CDN_BASE}/{version}/data/en_US/item.json"
    try:
        items = requests.get(url).json()["data"]
        os.makedirs(ITEM_FOLDER, exist_ok=True)

        for item_id, item_data in items.items():
            name = item_data["name"]
            image_url = f"{CDN_BASE}/{version}/img/item/{item_id}.png"
            file_path = os.path.join(ITEM_FOLDER, normalize(name))

            if not os.path.exists(file_path):
                r = requests.get(image_url)
                with open(file_path, "wb") as f:
                    f.write(r.content)
                print(f"✅ Item: {name}")
            else:
                print(f"✔️ Item already exists: {name}")
    except Exception as e:
        print("❌ Ошибка при скачивании предметов:", e)

if __name__ == "__main__":
    version = get_latest_version()
    if version:
        print(f"📦 Версия League of Legends: {version}")
        download_champions(version)
        download_items(version)
