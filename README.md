# Bank Widget Project

## Описание проекта

Этот проект представляет собой виджет для работы с банковскими операциями клиента. В проекте реализованы функции фильтрации и сортировки операций по состоянию и дате.

## Структура проекта

- src/processing/processing.py — модуль с функциями обработки данных.

## Реализованные функции

### filter_by_state(operations: list[dict], state: str = 'EXECUTED') -> list[dict]

Фильтрует список операций, возвращая только те, у которых ключ state соответствует заданному значению.

- Параметры:
  - operations — список словарей с операциями.
  - state — состояние операции (по умолчанию `'EXECUTED'`).

- Возвращает:
  - Новый список операций, отфильтрованный по состоянию.

### sort_by_date(operations: list[dict], descending: bool = True) -> list[dict]

Сортирует список операций по дате.

- Параметры:
  - operations — список словарей с операциями.
  - descending — порядок сортировки (по умолчанию True — от новых к старым).

- Возвращает:
  - Новый список операций, отсортированный по дате.

## Как использовать

1. Склонируйте репозиторий:

```bash
(git clone https://github.com/Viktoriiatsiklauri/bank_widget_project.gi)
```
2. Перейдите в директорию проекта:
cd bank_widget_project

3. Запустите Python и импортируйте функции:
from src.processing.processing import filter_by_state, sort_by_date

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

executed_ops = filter_by_state(operations)
sorted_ops = sort_by_date(executed_ops)

print(sorted_ops)

# Лицензия
MIT License

Тестирование
 • Все функции проекта тестируются в отдельных файлах тестов.
 • Используются фикстуры для генерации тестовых данных (например, для транзакций).
 • Применяется параметризация, чтобы проверять различные входные данные без дублирования кода.
 • При запуске pytest все тесты проходят успешно.

## Модуль generators

Модуль `generators` содержит функции для работы с большими массивами транзакций и генерации номеров карт:

### Функции

1.filter_by_currency(transactions: list[dict], currency: str).
   - Принимает список словарей с транзакциями.
   - Возвращает итератор, который выдаёт только транзакции с указанной валютой.
   - Пример использования:
   ```python
   usd_transactions = filter_by_currency(transactions, "USD")
   for tx in usd_transactions:
       print(tx)

 2. transaction_descriptions(transactions)
 - Принимает список словарей с транзакциями.
 - Возвращает генератор, выдающий описание каждой операции по очереди.
 - Пример использования:

descriptions = transaction_descriptions(transactions)
for desc in descriptions:
    print(desc)


 3. card_number_generator(start, stop)
 • Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.
 • Аргументы start и stop задают диапазон номеров карт.
 • Пример использования:

for card_number in card_number_generator(1, 5):
    print(card_number)


Тестирование
 • Для всех функций написаны тесты с использованием pytest.
 • Проверяется корректность работы функций и генераторов.
 • Используются фикстуры и параметризация для проверки разных кейсов.
 • Покрытие тестами функционального кода — более 80%.
 • HTML-отчет с покрытием создаётся командой:

pytest --cov=src --cov-report=html

 • Результат отчета сохраняется в папке htmlcov.