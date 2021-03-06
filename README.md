# Корпус анекдотов
Проект по курсу "Автоматическая обработка естественного языка", 3 курс

## О чём проект?
Это корпус анекдотов, по которому можно производить поиск по словоформе, лемме или POS-тегу.
* [Сайт](http://anecdotesdb.pythonanywhere.com/)
* [База данных](https://drive.google.com/drive/folders/11jUlZJfIS2ssr0RsTkpg9B_vW7cNam1n?usp=sharing)
* [Слайды презентации](https://docs.google.com/presentation/d/1bdji4dZrU0wHxqbTDjJDmA9Bws23Zu97Ckgf-dLfY54/edit?usp=sharing)
* [Сообщество в ВКонтакте](https://vk.com/a_story)

## Как реализован?
__Языки__:
* ЯП: Python
* ЯР: HTML, CSS
* ЯЗ: SQL для Python

__Библиотеки__:
* Парсинг: ``requests``, ``pandas``, ``csv``
* БД: ``sqlite3``, ``csv``
* Морфология: ``stanza``, ``nltk``, ``csv``
* Деплой: ``flask``
* Поиск: ``sqlite3``

* а ещё API: VK

Тексты для корпуса были собраны с сообщества ВКонтакте и помещены в базу данных. Тексты были обработаны с помощью бибилотеки ``nltk``, разметка текстов производилась с помощью библиотеки ``stanza`` (тег-сет Universal Dependencies). Поиск по корпусу реализован на сайте.

## Команда проекта
* Анна Мартынова, БКЛ-192 - фронтенд-разработчик, деплой
* Оксана Цегоева, БКЛ-192 - DS парсинг, деплой
* Дарья Ревенко, БКЛ-192 - NLP, поиск, художник-оформитель страницы помощи
* Янина Худина, БКЛ-191 - DS база данных, поиск, художник-оформитель репозитория
