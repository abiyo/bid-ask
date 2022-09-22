-----------------------------------------------------------------------------------------
Инструкция по запуску.

На запускаемом компьютере должны быть установлены docker, docker compose и git.

1. Склонировать репозиторий:
   ```git clone https://github.com/abiyo/bid-ask.git```
2. В корне проекта запустить docker compose:
   ```docker compose up -d --build```
Запуск может занять несколько минут.

В результате будет запущено 5 контейнеров:
- Приложение на Python
- PostgreSQL - в базу идет запись всех генереруемых json
- Pgadmin - для просмотра БД
- Elasticsearch - сюда дополнительно будут направляться только те json, которые соответствуют условию (bid_01+ask_01 < 120)
- Kibana - для просмотра Elasticsearch

Откройте Pgadmin 
```sh
http://localhost:5050/
```
```sh
User: admin@example.com
Pass: secretpass
```
В списке серверов откройте bidask. Появится окно ввода пароля.
```sh
Pass: secretpass
```
Данные записываются в базу bidask, таблица json_table.

Откройте Kibana 
```sh
http://localhost:5601/
```
В выпадающем меню в разделе Kibana выберите Discover.
В поле Index Pattern введите bidask. Далее Next Step и Create Index Pattern.
Снова в разделе Kibana выберите Discover.
Вы увидите записи, которые попадают в Elasticsearch согласно условию, определенному в python-приложении.


-------------------------------------------------- ------------------------------------
Startup instructions.

Docker, docker compose and git must be installed on the machine.

1. Clone the repository:
   ```git clone https://github.com/abiyo/bid-ask.git```
2. In the root of the project, run docker compose:
   ```docker compose up -d --build```
It may take several minutes to start.

As a result, 5 containers will be started:
- Python - application
- PostgreSQL - all generated json is written to the database
- Pgadmin - to view the database
- Elasticsearch - only those jsons that match the condition (bid_01+ask_01 < 120) will be sent here additionally
- Kibana - for browsing Elasticsearch

Open pgadmin
```sh
http://localhost:5050/
```
```sh
User: admin@example.com
Pass: secret pass
```
In the list of servers, open bidask. A password entry window will appear.
```sh
Pass: secret pass
```
The data is written to the bidask database, the json_table table.

Open Kibana
```sh
http://localhost:5601/
```
From the dropdown menu under "Kibana", select "Discover".
In the "Index Pattern" field, enter "bidask". Next "Next Step" and "Create Index Pattern".
Again, in the "Kibana" section, select "Discover".
You will see the records that fall into Elasticsearch according to the condition defined in the python application.