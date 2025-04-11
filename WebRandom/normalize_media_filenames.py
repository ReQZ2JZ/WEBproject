import os

def normalize_filename(name):
    return name.replace(" ", "").replace("'", "")

folders = {
    "champion_images": os.path.join("media", "champion_images"),
    "item_images": os.path.join("media", "item_images")
}

for label, path in folders.items():
    if not os.path.isdir(path):
        print(f"❌ Папка не найдена: {path}")
        continue

    for filename in os.listdir(path):
        old_path = os.path.join(path, filename)

        if not os.path.isfile(old_path):
            continue

        name, ext = os.path.splitext(filename)
        new_name = normalize_filename(name) + ext
        new_path = os.path.join(path, new_name)

        if old_path != new_path:
            os.rename(old_path, new_path)
            print(f"✅ {label}: {filename} → {new_name}")
