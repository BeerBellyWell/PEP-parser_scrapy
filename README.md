# Проект парсинга pep

>Парсит информацию о статусе всех существующих PEP. Со страниц PEP парсер собирает номер, название, статус и сохраняет в файле .csv

Стек: Python v3.9, Scrapy, Git.

#### Как запустить проект:

+ клонируем репозиторий `git clone`
`https://github.com/BeerBellyWell/scrapy_parser_pep`
+ переходим в него `cd scrapy_parser_pep`
    + разворачиваем виртуальное окружение
    `python3 -m venv env` (Windows: `python -m venv env`)
    + активируем его
    `source env/bin/activate` (Windows: `source env/scripts/activate`)
    + устанавливаем зависимости из файла requirements.txt
    `pip install -r requirements.txt`
+ запускаем парсер
`scrapy crawl pep`
