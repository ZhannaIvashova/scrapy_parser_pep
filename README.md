# Асинхронный парсер PEP.
## Описание
*Парсер выводит собранную информацию в два файла .csv. В первом файле список всех PEP: номер, название и статус, во втором файле сводка по статусам PEP — сколько найдено документов в каждом статусе (статус, количество). В последней строке этого файла выводится общее количество всех документов*
## Основные технологии
- Python 3.11
- Scrapy 2.5.1
## Адреса, использующиеся в проекте
- https://peps.python.org/
### Запуск проекта
- Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:ZhannaIvashova/scrapy_parser_pep.git
```
- Установите и активируйте виртуальное окружение
```
python -m venv venv
source venv/Scripts/activate
```
- Установите зависимости из файла requirements.txt
```
python -m pip install --upgrade pip
pip install -r requirements.txt
``` 
- Из директории scrapy_parser_pep запустить команду:
```
scrapy crawl pep
```
Будет создана папка results в директории scrapy_parser_pep и в ней два файла c примерным наименованием:
pep_2023-11-23T11-36-34.csv; status_summary_2023-11-23_14-36-41.csv

### Обратная связь
Контакт: [Жанна Ивашова](https://github.com/ZhannaIvashova)