# Данный учебный проект - одна из домашних работ по курсу Full-stack веб-разработчик на Python от компании SkillFactory.

По заданию нужно было сделать проект домашней библиотеки.
Книги с учетом количества экзепляров, Авторы книг, Издательства.
Дополнительно необходима возможность учитывать кому и какие книги были переданы.
Реализация на django 2.2.7 без использования JavaScript

Результат домашней работы реализован в приложении `p_library`.

Приложение для учета лекарств в домашней аптечке `my_first_aid_kit` пока не дописано. В мастер попало случайно =)

### Heroku deploy

Для разварачивания своей копии на облачной PaaS платформе Heroku можно воспользоваться следующим сценарием:

- на GitHub делаем форк проекта
- после регистрации на heroku.com создаем новое приложение (кнопка NEW -> Create New App)
- если в рамках учетной записи heroke пока не создана база данных переходим `https://data.heroku.com/`
- создаем базу данных `heroku-postgres`
- копируем URI базы
- возвращаемся в настройки преложения и вставляем URI базы в переменную окружения `"DATABASE_URL"` нового приложения
- после создания приложения во вкладке Deploy выбираем Deployment method - GitHub
- указываем ссылку на репозиторий GitHub с форком проекта
- проходим этап аутентификации и связываем GitHub с Heroku.
- настраиваем Automatic deploys
- выбираем правильный Deploy Branch
- если установлен heroku cli, запускаем команды (`__app__` необходимо заменить на название приложения heroku):
    - `heroku run --app __app__ python manage.py makemigrations p_library`
    - `heroku run --app __app__ python manage.py migrate`
- как вариант, сделать это через кансоль прямо на heroku.com (кнопка `more` -> `run console`)
- добавляем переменную окружения `'SECRET_KEY'` (случайный набор символов длинной 50 символов)
    - можно сгенерировать так :
    
    '''
    from django.utils.crypto import get_random_string
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    SECRET_KEY = get_random_string(50, chars)
    '''


### VDS deploy

Покупаем сервер, устанавливаем ОС, заходим по SSH....

При разворачивании на VDS сервере необходимо доставить необходимые пакеты. Лучше не в общую систему, а в виртуальное окружение virtualenv.
`pip install -r requirements.txt`

Клонируем проект с гитхаба

Создаем 

 Ключ прячем в файле 'my_site/secrets.py' (деплой на VDS)



 ToDo:

- почистить p_library от ненужных views. Несколько def views остались после перехода на CBV.
- добавить фильтры в books_list, authors_list и прочие.
- доделать my_first_aid_kit
