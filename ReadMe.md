# API_Transfer


## Задание

Необходимо реализовать *API* сервис, который поддерживает следующие функции:
- Создание нового груза (характеристики локаций pick-up, delivery определяются по введенному zip-коду);
- Получение списка грузов (локации pick-up, delivery, количество ближайших машин до груза (=< 450 миль));
- Получение информации о конкретном грузе по ID (локации pick-up, delivery, вес, описание, список номеров ВСЕХ машин с расстоянием до выбранного груза);
- Редактирование машины по ID (локация (определяется по введенному zip-коду));
- Редактирование груза по ID (вес, описание);
- Удаление груза по ID.
- Фильтр списка грузов (вес, мили ближайших машин до грузов);(не совсем понял фильтр по милям)
- Автоматическое обновление локаций всех машин раз в 3 минуты (локация меняется на другую случайную).(не реализовано)
### Структура БД

Груз обязательно должен содержать следующие характеристики:
- локация pick-up;
- локация delivery;
- вес (1-1000);
- описание.

Машина обязательно должна в себя включать следующие характеристики:
- уникальный номер (цифра от 1000 до 9999 + случайная заглавная буква английского алфавита в конце, пример: "1234A", "2534B", "9999Z")
- текущая локация;
- грузоподъемность (1-1000).

Локация должна содержать в себе следующие характеристики:
- город;
- штат;
- почтовый индекс (zip);
- широта;
- долгота.

## Доступные endpoint-ы
```
loads/ (POST)
loads/ (GET)
loads/{id}/ (GET)
loads/{id}/ (PUT)
loads/{id}/ (PATCH)
loads/{id}/ (DELETE)
loads/?ordering=(weight or -weight) (GET)
cars/ (POST)
cars/ (GET)
cars/{id}/ (GET)
cars/{id}/ (PUT)
cars/{id}/ (PATCH)
cars/{id}/ (DELETE)
```

## Пример запросов и ответов API
- POST - запрос на endpoint `loads/`, создание объекта груза, поля: `pick_up` и `delivery` принимают zip-индексы.
```
{
  "pick_up": 617,
  "delivery_to": 690,
  "weight": 600,
  "description": "random description"
}
```
Ответ:
```
{
  "pick_up": 617,
  "delivery_to": 690,
  "weight": 600,
  "description": "random description"
}
```


## Для загрузки `uszips.csv` создана команда:

```
python manage.py import_to_db
```
## Для создания 20 машин по умолчанию создана команда:

```
python manage.py create_default_cars
```

## Установка и запуск проекта

1. Клонируйте репозиторий:
```
git clone https://github.com/old4visst/API_Transfer.git
```
2. Выполните команды в терминале в папке проекта:
```
docker compose build
docker compose up -d
docker compose run --rm web-app sh -c "python manage.py migrate"
docker compose run --rm web-app sh -c "python manage.py import_to_db"
docker compose run --rm web-app sh -c "python manage.py create_default_cars"
docker compose restart
```
