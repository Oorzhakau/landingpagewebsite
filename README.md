# Проект landingpagewebsite – сайт для стоматологии.

Проект **landingpagewebsite** – коммерческий веб-сайт с административной панелью, CRM системой, управлением контентом и Telegram-ботом для отправки оповещений.

Сайт развернут на Яндекс.Облаке на образе debian 11.

**Url** - https://tuvadentistry.ru/.

___

## Установка:
1. Клонируйте репозиторий на локальную машину.

``git clone https://github.com/Oorzhakau/landingpagewebsite``
2. Установите виртуальное окружение.

``python -m venv venv`` 

 или
 
 ``python3 -m venv venv``
3. Активируйте виртуальное окружение.

``source venv\Scripts\activate``

или

``venv\bin\activate``
5. Установите зависимости.

``pip install -r requirements.txt``
6. Запустите локальный сервер.

``python manage.py runserver``
7. Создаете суперюзера.

``python manage.py createsuperuser``
8. Задаем chat_id и токен бота через CRM систему.

## Технологии
Djagno==4.0

___

## Список исполнителей:

**[Александр Ооржак](https://github.com/Oorzhakau)**
