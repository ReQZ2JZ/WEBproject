import json
import logging
import os
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

# Настройки
BASE_URL = "https://api.hearthstonejson.com/v1/latest/ruRU/cards.json"  # JSON с картами (русская локаль)
OUTPUT_DIR = "static/images/hearthstone"  # Папка для сохранения
MAX_WORKERS = 8  # Количество потоков
LOG_FILE = "download_errors.log"  # Лог ошибок
FAILED_CARDS_JSON = "failed_cards.json"  # JSON для пропущенных карт
RETRY_ATTEMPTS = 3  # Количество попыток
RETRY_DELAY = 2  # Задержка между попытками (сек)

def setup_logging():
    """Настраивает логирование ошибок."""
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        filemode="w"
    )

def create_output_dir(directory):
    """Создает папку для изображений, если она не существует."""
    Path(directory).mkdir(parents=True, exist_ok=True)

def download_image(card, output_dir, failed_cards):
    """Скачивает изображение одной карты с повторными попытками."""
    card_id = card.get("id")
    card_name = card.get("name", "Неизвестно")

    if not card_id:
        logging.info(f"Пропущена карта '{card_name}': нет ID")
        print(f"Пропущена карта '{card_name}': нет ID")
        failed_cards.append({"name": card_name, "reason": "Нет ID"})
        return

    img_url = f"https://art.hearthstonejson.com/v1/512x/{card_id}.png"
    file_name = f"{card_id}.png"
    file_path = os.path.join(output_dir, file_name)

    # Пропускаем существующие файлы
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        print(f"Карта '{card_name}' ({card_id}) уже загружена")
        return

    for attempt in range(RETRY_ATTEMPTS):
        try:
            response = requests.get(img_url, stream=True, timeout=10)
            if response.status_code == 200:
                with open(file_path, "wb") as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                # Проверяем целостность файла
                if os.path.getsize(file_path) > 1000:  # Минимум 1KB для изображения
                    print(f"Скачана карта: {card_name} ({card_id})")
                    return
                else:
                    os.remove(file_path)  # Удаляем поврежденный файл
                    logging.info(f"Поврежденное изображение для '{card_name}' ({card_id}), попытка {attempt + 1}")
            else:
                logging.info(f"Ошибка загрузки '{card_name}' ({card_id}): статус {response.status_code}, попытка {attempt + 1}")
                print(f"Ошибка загрузки '{card_name}' ({card_id}): статус {response.status_code}, попытка {attempt + 1}")
        except requests.RequestException as e:
            logging.info(f"Сетевая ошибка для '{card_name}' ({card_id}): {e}, попытка {attempt + 1}")
            print(f"Сетевая ошибка для '{card_name}' ({card_id}): {e}, попытка {attempt + 1}")

        if attempt < RETRY_ATTEMPTS - 1:
            time.sleep(RETRY_DELAY)

    # Если загрузка не удалась
    logging.info(f"Не удалось загрузить '{card_name}' ({card_id}) после {RETRY_ATTEMPTS} попыток")
    print(f"Не удалось загрузить '{card_name}' ({card_id}) после {RETRY_ATTEMPTS} попыток")
    failed_cards.append({"id": card_id, "name": card_name, "reason": "Изображение недоступно"})

def main():
    # Настраиваем логирование
    setup_logging()

    # Создаем папку для изображений
    create_output_dir(OUTPUT_DIR)

    # Список для пропущенных карт
    failed_cards = []

    # Получаем данные о картах
    print("Загружаем данные о картах...")
    try:
        response = requests.get(BASE_URL, timeout=10)
        response.raise_for_status()
        cards = response.json()
    except requests.RequestException as e:
        print(f"Ошибка загрузки JSON: {e}")
        logging.error(f"Ошибка загрузки JSON: {e}")
        return

    # Фильтруем только коллекционные карты
    collectible_cards = [card for card in cards if card.get("collectible", False)]
    print(f"Найдено {len(collectible_cards)} коллекционных карт")

    # Скачиваем изображения параллельно
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        executor.map(
            lambda card: download_image(card, OUTPUT_DIR, failed_cards),
            collectible_cards
        )

    # Сохраняем данные о пропущенных картах
    if failed_cards:
        with open(FAILED_CARDS_JSON, "w", encoding="utf-8") as f:
            json.dump(failed_cards, f, ensure_ascii=False, indent=2)
        print(f"Пропущенные карты сохранены в {FAILED_CARDS_JSON}")

    print("Загрузка завершена! Ошибки записаны в", LOG_FILE)

if __name__ == "__main__":
    main()