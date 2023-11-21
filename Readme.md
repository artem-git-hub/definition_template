# Сервис определения шаблонов

## Запуск

### Перед запуском у вас должны быть установленны утилиты:
- docker  
- docker-compose  

1. Склонировать и зайти в дирректорию:
```shell
git clone https://github.com/artem-git-hub/definition_template.git
cd definition_template
```

2. Выполнить команду для сборки приложения:
```shell
sudo docker-compose up --build
```

## Использование

**Базовая авто-документация:** `http:localhost:8000/docs`

**POST: /get_form**  
Пример тела (body) запроса:
```json
{
    "name": "Bob",
    "email": "mebob@mail.ru",
    "phone": "+7 888 888 88 88",
    "date": "12.12.2000"
}
```
или
```json
{
    "name": "Bob",
    "date": "12.12.2000",
    "description": "me a send desc"
}
```

*В первом случае выдаст имя шаблона (см. ниже добавленные шаблоны), во втором типы переданных данных*


**Добавлены базовые шаблоны для проверки (db/templates.json)**  
```json
[
    {
        "template_name": "Base template",
        "fields": {
            "name": "text",
            "email": "email",
            "date": "date"
        }
    },
    {
        "template_name": "Base template 2",
        "fields": {
            "phone": "phone",
            "date": "date"
        }
    }
]
```