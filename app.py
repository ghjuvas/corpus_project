from flask import Flask, render_template, request
# import sqlite3
from models import db, Words, Metainformation, Sentences
from search_mod import main

app = Flask(__name__, template_folder='templates')
# что-то сейчас не могу сообразить, пондаобится ли оно в принципе
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anecdotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)


@app.route('/')
def index():
    '''
    Вывод страницы поиска
    '''

    return render_template('index.html')

@app.route('/help')
def help():
    '''
    Вывод страницы поиска
    '''
    return render_template('help.html')

@app.route('/results', methods=['get', 'post'])
def results():
    '''
    Вывод страницы с результатами.
    Собирает данные пользователя, ищет по базе данных
    '''

    # если нет аргументов, то будем выводить страницу с Басей
    if not request.values:
        return render_template('empty.html')

    else:

        content1 = request.args.get('input1')

        # если первого аргумента нет, то тоже страница с кошкошибкой
        if content1 == '':
            return render_template('empty.html')

        else:

            final_req = []

            content2 = request.args.get('input2')
            content3 = request.args.get('input3')
            type1 = request.args.get('type1')
            type2 = request.args.get('type2')
            type3 = request.args.get('type3')

            final_req.append((content1, type1))

            # второй слот может быть пустым - считаем, что это любое слово?
            full_req = {
                content2: type2,
                content3: type3
            }

            for item in full_req.items():
                if item[0] != '':
                    final_req.append(item)

            search_res = main(final_req)

        if len(search_res) == 0:
            return render_template('empty.html')
        else:
            length = len(search_res)
            return render_template('results.html', leg=length, search_res=search_res)


    # запись запросов в бд
    # req = Request(
    #     input1=input_1,
    #     input2=input_2,
    #     input3=input_3
    # )

    # db.session.add(req)
    # db.session.commit()
    # db.session.refresh(req)

    # cюда надо передать то, что будет выдаваться на страницу


if __name__ == '__main__':
    app.run(debug=False)
