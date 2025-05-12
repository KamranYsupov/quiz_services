#  Запуск проекта

<h4>
1. Создайте файл .env в корневой директории 
проекта и установите переменные согласно .env.example:
</h4>

```requirements
API_SERVICE_NAME=
BOT_TOKEN=

JAEGER_HOST=jaeger
JAEGER_PORT=6831

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=db
DB_PORT=5432

REDIS_HOST=
REDIS_PORT=
```

<h4>
2. Запустите docker compose:
</h4>

```commandline
docker compose up --build -d
```


<h4>
3. Отправьте боту комманду /start
</h4>
<br>

<b>Готово!</b><br>
<b>Документация API:</b> <em>http://127.0.0.1/docs</em><br>
<b>Трейсинг запросов(Jaуger UI):</b> <em>http://127.0.0.1:16686/search</em><br>

</h4>
