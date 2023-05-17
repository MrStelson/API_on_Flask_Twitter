# Разработка API на Flask 

## Для запуска приложения:
  1.Устанавливаем виртуальное окружение
```
    virtualenv env
    source env/bin/activate
```
  2.Устанавливаем зависимости
```
    pip install -r requirements.txt
```
  3. Запустить app.py через терминал: $
```
    python main.py
```


### 1. Создать твит:
Необходимо отправить POST запрос на url: localhost:5000/twit в формате .json </br>
Пример тела запроса: </br>

{"id": "1","body":"new_twit", "author": {"id": "1", "username": "new_author"}}

### 2. Получить все твиты:
Необходимо отправить GET запрос на url: localhost:5000/twits

### 3. Получить твит по id:
Необходимо отправить POST запрос на url: localhost:5000/get_twit_by_id в формате .json </br>
Пример тела запроса: </br>
{"id": "1"}

### 4. Обновить твит:
Необходимо отправить POST запрос на url: localhost:5000/update_twit_by_id в формате .json </br>
Пример тела запроса: </br>
{"id": "1","body":"new_twit_updated", "author": {"id": "2", "username": "new_author"}}

### 5. Удалить твит:
Необходимо отправить POST запрос на url: localhost:5000/twit/delete в формате .json </br>
Пример тела запроса: </br>
{"id": "1"}

### 6. Добавить комментарий к посту:
Необходимо отправить POST запрос на url: localhost:5000/add_comment в формате .json </br>
Пример тела запроса: </br>
{"twit_id": "1", "comment_id": "1", "body": "new_comment", "author" : "new_author1"}

### 7. Удалить комментарий к посту:
Необходимо отправить POST запрос на url: localhost:5000/del_comment в формате .json </br>
Пример тела запроса: </br>
{"twit_id": "1", "comment_id": "1"}