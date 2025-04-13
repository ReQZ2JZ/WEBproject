import requests
import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

# Настройки
BASE_URL = "https://api.hearthstonejson.com/v1/latest/enUS/cards.json"  # JSON со всеми картами (enUS)
OUTPUT_DIR = "static/images/hearthstone"  # Папка для сохранения изображений
MAX_WORKERS = 10  # Количество потоков для параллельной загрузки

def create_output_dir(directory):
    """Создает папку для изображений, если она не существует."""
    Path(directory).mkdir(parents=True, exist_ok=True)

def download_image(card, output_dir):
    """Скачивает изображение одной карты."""
    card_id = card.get("id")
    img_url = card.get("img")  # URL изображения карты
    if not img_url or not card_id:
        print(f"Пропущена карта {card.get('name', 'без имени')}: нет URL или ID")
        return

    file_name = f"{card_id}.png"
    file_path = os.path.join(output_dir, file_name)

    try:
        response = requests.get(img_url, stream=True, timeout=10)
        if response.status_code == 200:
            with open(file_path, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Скачана карта: {card.get('name')} ({card_id})")
        else:
            print(f"Ошибка загрузки {card_id}: статус {response.status_code}")
    except requests.RequestException as e:
        print(f"Ошибка загрузки {card_id}: {e}")

def main():
    # Создаем папку для изображений
    create_output_dir(OUTPUT_DIR)

    # Получаем данные о картах
    print("Загружаем данные о картах...")
    try:
        response = requests.get(BASE_URL, timeout=10)
        response.raise_for_status()
        cards = response.json()
    except requests.RequestException as e:
        print(f"Ошибка загрузки JSON: {e}")
        return

    # Фильтруем только коллекционные карты (collectible=True)
    collectible_cards = [card for card in cards if card.get("collectible", False)]
    print(f"Найдено {len(collectible_cards)} коллекционных карт")

    # Скачиваем изображения параллельно
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(
            lambda card: download_image(card, OUTPUT_DIR),
            collectible_cards
        )

    print("Загрузка завершена!")

if __name__ == "__main__":
    main()