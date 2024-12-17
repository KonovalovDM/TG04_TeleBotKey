# TG04_TeleBotKey
 TeleBotKey

Телеграмм Бот с простым меню с кнопками:<br>
### 1-й Бот:

При отправке команды __/start__ бот будет показывать меню с кнопками **"Привет"** и **"Пока"**. При нажатии на кнопку **"Привет"** бот будет отвечать *"Привет, {имя пользователя}!"*, а при нажатии на кнопку **"Пока"** бот будет отвечать *"До свидания, {имя пользователя}!"*.

### 2-й Бот: Кнопки с URL-ссылками

При отправке команды **/links** бот будет показывать инлайн-кнопки с URL-ссылками. Созданы три кнопки с ссылками на новости/музыку/видео

### 3-й Бот: Динамическое изменение клавиатуры

При отправке команды **/dynamic** бот будет показывать инлайн-кнопку **"Показать больше"**. При нажатии на эту кнопку бот заменит её на две новые кнопки *"Опция 1"* и *"Опция 2"*. При нажатии на любую из этих кнопок бот отправляет сообщение с текстом выбранной опции.
<br>___Структура проекта:___
```
├── main.py            # Основной файл с логикой бота
├── keyboards.py       # Файл с клавиатурами
├── config.py          # Конфигурационный файл с токеном
```