import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Этапы проекта с новыми сроками
tasks = [
    ("Анализ и требования", "2025-04-07", "2025-04-15"),
    ("Логика генерации", "2025-04-15", "2025-04-25"),
    ("Разработка UI", "2025-04-25", "2025-05-06"),
    ("Тестирование и баланс", "2025-05-06", "2025-05-15"),
    ("Документация и GitHub", "2025-05-15", "2025-06-01")
]

# Подготовка данных
y_pos = range(len(tasks))
start_dates = [datetime.strptime(start, "%Y-%m-%d") for _, start, _ in tasks]
end_dates = [datetime.strptime(end, "%Y-%m-%d") for _, _, end in tasks]
durations = [(end - start).days for start, end in zip(start_dates, end_dates)]

# Построение графика
fig, ax = plt.subplots(figsize=(10, 6))

for i, (start, duration) in enumerate(zip(start_dates, durations)):
    ax.barh(i, duration, left=start, height=0.4, align='center', color='skyblue', edgecolor='black')

# Настройки визуала
ax.set_yticks(list(y_pos))
ax.set_yticklabels([task[0] for task in tasks])
ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
plt.xticks(rotation=45)
plt.xlabel("Дата")
plt.title("Диаграмма Ганта проекта GearShuffle")
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()

# Сохранение
plt.savefig("gearshuffle_gantt_chart_updated.png")
plt.show()
