# Представь что ты анализируешь проект на фрилансе
budget = 260        # бюджет клиента в долларах
deadline_days = 7   # сколько дней на выполнение
is_clear_task = True  # понятно ли задание

print("=== АНАЛИЗ ЗАКАЗА ===")

if budget < 50:
    print("❌ Бюджет слишком маленький, не берём")
elif budget >= 50 and deadline_days >= 3 and is_clear_task:
    print("✅ Отличный заказ, берём!")
    earnings = budget * 0.9  # минус комиссия платформы 10%
    print("Заработаем:", earnings, "$")
elif budget >= 50 and deadline_days < 3:
    print("⚠️ Бюджет хороший, но срок слишком короткий")
else:
    print("🤔 Нужно уточнить детали у клиента")