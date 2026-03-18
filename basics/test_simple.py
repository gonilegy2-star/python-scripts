# Сколько часов ты уже практиковался в программировании
hours = 53  # пока у нас 2 часа (2 дня по 1 часу)

if hours < 10:
    level = "Новичок"
    next_step = "Учи основы Python"
elif hours < 50:
    level = "Начинающий"
    next_step = "Переходи к AI инструментам"
elif hours < 150:
    level = "Средний"
    next_step = "Делай первые проекты"
else:
    level = "Продвинутый"
    next_step = "Выходи на фриланс"

print("Твой уровень:", level)
print("Следующий шаг:", next_step)
print("Часов накоплено:", hours)