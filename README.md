## Установка

1. установить интерпритатор python версии 3.11+
2. python -m venv env
3. source env/bin/activate
4. pip install -U pip && pip install -r requirements.txt
5. deactivate
6. echo '<Любая строчка>' >> '.password_salt

## Запуск

1. Перейти в корневую директорию проекта
2. env/bin/python main

## Добавление нового пользователя

1. Перейти в корневую директорию проекта
2. env/bin/python main -n
