import requests
from bs4 import BeautifulSoup
import os
import urllib.request

# Укажи папку для сохранения изображений (абсолютный путь с учётом пробела)
output_dir = r"C:\Users\Пин Код\Documents\GitHub\WEBproject\WebRandom\static\images\forza_horizon5\cars"

# Создаём папку, если она не существует (включая промежуточные директории)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# URL страницы со списком автомобилей (forza.net/cars)
url = "https://forza.net/cars"  # Укажи точный URL, если он отличается

# Заголовки для имитации браузера
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    # Отправляем запрос на сайт
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Проверяем, что запрос успешен

    # Парсим HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Ищем все теги <img> (адаптируй селектор под сайт)
    img_tags = soup.find_all("img", class_="car-image")  # Укажи правильный класс

    if not img_tags:
        print("Не удалось найти изображения. Проверь селектор или структуру сайта.")
    else:
        print(f"Найдено {len(img_tags)} изображений.")

        # Скачиваем каждое изображение
        for idx, img in enumerate(img_tags):
            img_url = img.get("src")
            if not img_url:
                continue

            # Если URL относительный, добавляем базовый домен
            if not img_url.startswith("http"):
                img_url = "https://forza.net" + img_url

            # Имя файла
            car_name = img.get("alt", f"car_{idx}").replace(" ", "_").replace("/", "_")
            file_extension = img_url.split(".")[-1]
            file_name = f"{car_name}.{file_extension}"
            file_path = os.path.join(output_dir, file_name)

            try:
                print(f"Скачиваем {img_url} как {file_name}...")
                urllib.request.urlretrieve(img_url, file_path)
                print(f"Сохранено: {os.path.abspath(file_path)}")
            except Exception as e:
                print(f"Ошибка при скачивании {img_url}: {e}")

except requests.exceptions.RequestException as e:
    print(f"Ошибка при запросе к сайту: {e}")

print("Скачивание завершено!")