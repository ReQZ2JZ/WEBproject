import random

def generate_forza_horizon5_build(car_class=None):
    cars = [
        {"name": "Lamborghini Aventador", "image": "lamborghini_aventador.png", "class": "S1"},
        {"name": "Ferrari 488 GTB", "image": "ferrari_488_gtb.png", "class": "S2"},
        {"name": "Porsche 911 Turbo S", "image": "FH5_Porsche_911_Turbo_S_2023.png", "class": "S1"},
        {"name": "Abarth 124 Spider", "image": "abarth_124_spider.png", "class": "B"},  # Новая машина
    ]

    # Фильтруем автомобили по классу, если он указан
    if car_class:
        cars = [car for car in cars if car["class"] == car_class]

    # Если нет машин для указанного класса, возвращаем случайную машину
    if not cars:
        car = random.choice(cars)
    else:
        car = random.choice(cars)

    return {
        "car_name": car["name"],
        "car_image": f"/static/images/forza_horizon5/cars/{car['image']}",
        "car_class": car["class"],
    }