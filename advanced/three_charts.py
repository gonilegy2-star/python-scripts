import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_theme(style="whitegrid")

# 12 месяцев продаж по 3 категориям товаров
месяцы = ["Янв", "Фев", "Мар", "Апр", "Май", "Июн",
          "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек"]

электроника  = [45, 52, 48, 61, 58, 72, 69, 75, 82, 91, 110, 130]
одежда       = [38, 35, 55, 60, 65, 58, 52, 48, 62, 70, 95, 115]
продукты     = [80, 78, 82, 85, 88, 90, 92, 89, 87, 91, 95, 100]

# DataFrame для удобства
df_продажи = pd.DataFrame({
    "месяц":        месяцы,
    "электроника":  электроника,
    "одежда":       одежда,
    "продукты":     продукты
})

# данные по сотрудникам для корреляции
df_сотрудники = pd.DataFrame({
    "опыт":     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "зарплата": [35, 42, 48, 55, 63, 72, 80, 85, 92, 98, 105, 115],
    "продажи":  [20, 28, 35, 45, 52, 61, 70, 74, 82, 89, 94, 102],
    "город":    ["Москва", "Питер", "Москва", "Казань", "Питер",
                 "Москва", "Казань", "Москва", "Питер", "Москва",
                 "Казань", "Питер"]
})

print("Данные созданы!")
print(df_продажи)
plt.figure(figsize=(12, 5))

plt.plot(месяцы, электроника,
         marker="o", linewidth=2,
         color="steelblue", label="Электроника")

plt.plot(месяцы, одежда,
         marker="s", linewidth=2,
         color="coral", label="Одежда")

plt.plot(месяцы, продукты,
         marker="^", linewidth=2,
         color="green", label="Продукты")

# добавляем среднюю линию для электроники
среднее = np.mean(электроника)
plt.axhline(y=среднее, color="steelblue",
            linestyle="--", alpha=0.5,
            label=f"Среднее электроника ({среднее:.0f})")

plt.title("Тренд продаж по месяцам", fontsize=14)
plt.xlabel("Месяц")
plt.ylabel("Продажи (тыс. руб)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("1_тренд.png", dpi=150)
plt.show()

print("Максимум электроника:", max(электроника), "в", месяцы[электроника.index(max(электроника))])
print("Максимум одежда:", max(одежда), "в", месяцы[одежда.index(max(одежда))])
plt.figure(figsize=(10, 6))

# считаем итоги за год
итоги = {
    "Электроника": sum(электроника),
    "Одежда":      sum(одежда),
    "Продукты":    sum(продукты)
}

цвета = ["steelblue", "coral", "green"]
столбцы = plt.bar(
    итоги.keys(),
    итоги.values(),
    color=цвета,
    width=0.5,
    edgecolor="white",
    linewidth=1.5
)

# добавляем числа над столбцами
for столбец in столбцы:
    высота = столбец.get_height()
    plt.text(
        столбец.get_x() + столбец.get_width() / 2,
        высота + 5,
        f"{высота} тыс.",
        ha="center", va="bottom",
        fontsize=11, fontweight="bold"
    )

plt.title("Сравнение продаж по категориям за год", fontsize=14)
plt.xlabel("Категория")
plt.ylabel("Сумма продаж (тыс. руб)")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("2_сравнение.png", dpi=150)
plt.show()

print("\nИтоги за год:")
for категория, сумма in итоги.items():
    print(f"  {категория}: {сумма} тыс. руб")
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle("Корреляция: Опыт vs Зарплата и Продажи", fontsize=14)

# левый график — опыт vs зарплата
sns.scatterplot(
    data=df_сотрудники,
    x="опыт",
    y="зарплата",
    hue="город",
    size="продажи",
    sizes=(50, 250),
    palette="Set1",
    alpha=0.8,
    ax=axes[0]
)

# линия тренда
z = np.polyfit(df_сотрудники["опыт"], df_сотрудники["зарплата"], 1)
p = np.poly1d(z)
axes[0].plot(df_сотрудники["опыт"], p(df_сотрудники["опыт"]),
             "k--", alpha=0.5, label="Тренд")

axes[0].set_title("Опыт vs Зарплата")
axes[0].set_xlabel("Опыт (лет)")
axes[0].set_ylabel("Зарплата (тыс. руб)")
axes[0].legend()

# правый график — тепловая карта корреляций
корреляция = df_сотрудники[["опыт", "зарплата", "продажи"]].corr()

sns.heatmap(
    корреляция,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1, vmax=1,
    square=True,
    ax=axes[1],
    linewidths=0.5
)
axes[1].set_title("Матрица корреляций")

plt.tight_layout()
plt.savefig("3_корреляция.png", dpi=150)
plt.show()

# выводим корреляцию числами
print("\nКорреляция опыт-зарплата:",
      round(df_сотрудники["опыт"].corr(df_сотрудники["зарплата"]), 2))
print("Корреляция опыт-продажи:",
      round(df_сотрудники["опыт"].corr(df_сотрудники["продажи"]), 2))