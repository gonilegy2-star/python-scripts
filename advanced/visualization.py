import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_theme(style="whitegrid")

df = pd.DataFrame({
    "имя":      ["Данил", "Иван", "Мария", "Алексей", "Ольга",
                 "Дмитрий", "Анна", "Павел", "Елена", "Сергей"],
    "возраст":  [20, 25, 22, 30, 28, 35, 19, 27, 32, 24],
    "город":    ["Москва", "Питер", "Москва", "Казань", "Питер",
                 "Москва", "Казань", "Питер", "Москва", "Казань"],
    "баланс":   [1500, 3200, 800, 5000, 1200, 7500, 500, 4100, 2300, 3800],
    "зарплата": [50000, 75000, 45000, 100000, 60000, 120000, 35000, 85000, 70000, 80000],
    "опыт":     [1, 3, 1, 7, 4, 10, 0, 5, 6, 3]
})

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle("Анализ данных", fontsize=16)

# 1. Линейный — зарплата по опыту
axes[0, 0].plot(
    df.sort_values("опыт")["опыт"],
    df.sort_values("опыт")["зарплата"],
    marker="o", color="steelblue", linewidth=2
)
axes[0, 0].set_title("Зарплата по опыту")
axes[0, 0].set_xlabel("Опыт")
axes[0, 0].set_ylabel("Зарплата")

# 2. Барный — средняя зарплата по городам
средние = df.groupby("город")["зарплата"].mean()
axes[0, 1].bar(средние.index, средние.values, color=["steelblue", "coral", "green"])
axes[0, 1].set_title("Средняя зарплата по городам")
axes[0, 1].set_ylabel("Зарплата")

# 3. Гистограмма — распределение зарплат
axes[0, 2].hist(df["зарплата"], bins=8, color="purple", edgecolor="white")
axes[0, 2].set_title("Распределение зарплат")
axes[0, 2].set_xlabel("Зарплата")

# 4. Heatmap — корреляция
корреляция = df[["возраст", "баланс", "зарплата", "опыт"]].corr()
sns.heatmap(корреляция, annot=True, fmt=".2f", cmap="coolwarm",
            ax=axes[1, 0], square=True)
axes[1, 0].set_title("Корреляция")

# 5. Boxplot — зарплаты по городам
sns.boxplot(data=df, x="город", y="зарплата",
            palette="Set2", ax=axes[1, 1])
axes[1, 1].set_title("Зарплаты по городам")

# 6. Scatterplot — опыт vs зарплата
sns.scatterplot(data=df, x="опыт", y="зарплата",
                hue="город", size="баланс",
                sizes=(50, 200), ax=axes[1, 2])
axes[1, 2].set_title("Опыт vs Зарплата")

plt.tight_layout()
plt.savefig("полный_анализ.png", dpi=150)
plt.show()
print("Сохранено в полный_анализ.png")