import logging

# Создаем логгер
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG) # Общий уровень логгера

# 1. Создаем обработчик для записи в файл
file_handler = logging.FileHandler('app_log.txt', mode='a', encoding='utf-8')
file_handler.setLevel(logging.ERROR) # В ФАЙЛ пишем только ошибки

# 2. Создаем обработчик для вывода в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG) # В КОНСОЛИ видим всё

# 3. Создаем формат (как будет выглядеть строка)
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Добавляем обработчики к логгеру
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Тестируем
logger.debug("Это увидим только в консоли")
logger.error("Это увидим и в консоли, и в файле app_log.txt!")