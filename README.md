# django_interview_test



Задание для собеседования. Парсинг сайтов с указанной задержкой. 
- Работает на **Python 2.5** - **Python 3.6**. 
- Для парсинга использовались потоки (Thread) и очереди (Queue).

# Установка

## 1. Клонируйте репозиторий с помощью терминала
```sh
git clone https://github.com/romanyakovlev/django_interview_test
```

## 2. Активируйте виртуальное окружение для проекта

## 3. Установите необходимые зависимости
```sh
pip install -r requirements.txt
```
## 4. Выполните миграции для модели
```sh
python manage.py makemigrations
```
```sh
python manage.py migrate
```
## 5. Для добавления сайтов создайте пользователя в Django
```sh
python manage.py createsuperuser
```


## 6. Запустите проект
```sh
python manage.py runserver localhost:8000
```
Зайдите в панель администратора и создайте объекты для парсинга. Запустите процесс парсинга
