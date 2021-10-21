import sqlite3

# лемма (1ый запрос)
lemma_1 = '''
SELECT morph_parse.id, morph_parse.text_id, morph_parse.sent_id, sent, link
FROM morph_parse
JOIN texts_meta ON morph_parse.text_id = texts_meta.id
JOIN sents ON morph_parse.text_id = sents.text_id AND morph_parse.sent_id = sents.sent_id
WHERE lemma = ?
'''

# словоформа (1ый запрос)
word_1 = '''
SELECT morph_parse.id, morph_parse.text_id, morph_parse.sent_id, sent, link
FROM morph_parse
JOIN texts_meta ON morph_parse.text_id = texts_meta.id
JOIN sents ON morph_parse.text_id = sents.text_id AND morph_parse.sent_id = sents.sent_id
WHERE token = ?
'''

# тег (1ый запрос)
pos_1 = '''
SELECT morph_parse.id, morph_parse.text_id, morph_parse.sent_id, sent, link
FROM morph_parse
JOIN texts_meta ON morph_parse.text_id = texts_meta.id
JOIN sents ON morph_parse.text_id = sents.text_id AND morph_parse.sent_id = sents.sent_id
WHERE POS = ?
'''

# лемма+тег (1ый запрос)
lemma_pos_1 = '''
SELECT morph_parse.id, morph_parse.text_id, morph_parse.sent_id, sent, link
FROM morph_parse
JOIN texts_meta ON morph_parse.text_id = texts_meta.id
JOIN sents ON morph_parse.text_id = sents.text_id AND morph_parse.sent_id = sents.sent_id
WHERE lemma = ? AND POS = ?
'''

# словоформа+тег (1ый запрос)
word_pos_1 = '''
SELECT morph_parse.id, morph_parse.text_id, morph_parse.sent_id, sent, link
FROM morph_parse
JOIN texts_meta ON morph_parse.text_id = texts_meta.id
JOIN sents ON morph_parse.text_id = sents.text_id AND morph_parse.sent_id = sents.sent_id
WHERE token = ? AND POS = ?
'''

# лемма (2ой)
lemma_2 = '''
SELECT morph_parse.id, morph_parse.text_id, morph_parse.sent_id, sent, link
FROM morph_parse
JOIN texts_meta ON morph_parse.text_id = texts_meta.id
JOIN sents ON morph_parse.text_id = sents.text_id AND morph_parse.sent_id = sents.sent_id
WHERE lemma = ? AND morph_parse.text_id = ? AND morph_parse.id = ?
'''

# словоформа (2ой)
word_2 = '''
SELECT morph_parse.id, morph_parse.text_id, morph_parse.sent_id, sent, link
FROM morph_parse
JOIN texts_meta ON morph_parse.text_id = texts_meta.id
JOIN sents ON morph_parse.text_id = sents.text_id AND morph_parse.sent_id = sents.sent_id
WHERE token = ? AND morph_parse.text_id = ? AND morph_parse.id = ?
'''

# тег (2ой)
pos_2 = '''
SELECT morph_parse.id, morph_parse.text_id, morph_parse.sent_id, sent, link
FROM morph_parse
JOIN texts_meta ON morph_parse.text_id = texts_meta.id
JOIN sents ON morph_parse.text_id = sents.text_id AND morph_parse.sent_id = sents.sent_id
WHERE POS = ? AND morph_parse.text_id = ? AND morph_parse.id = ?
'''

# лемма+тег (2ой)
lemma_pos_2 = '''
SELECT morph_parse.id, morph_parse.text_id, morph_parse.sent_id, sent, link
FROM morph_parse
JOIN texts_meta ON morph_parse.text_id = texts_meta.id
JOIN sents ON morph_parse.text_id = sents.text_id AND morph_parse.sent_id = sents.sent_id
WHERE lemma = ? AND POS = ? AND morph_parse.text_id = ? AND morph_parse.id = ?
'''

# словоформа+тег (2ой)
word_pos_2 = '''
SELECT morph_parse.id, morph_parse.text_id, morph_parse.sent_id, sent, link
FROM morph_parse
JOIN texts_meta ON morph_parse.text_id = texts_meta.id
JOIN sents ON morph_parse.text_id = sents.text_id AND morph_parse.sent_id = sents.sent_id
WHERE token = ? AND POS = ? AND morph_parse.text_id = ? AND morph_parse.id = ?
'''

con = sqlite3.connect('../anecdotes.db', check_same_thread=False)
cur = con.cursor()


def search_1st_word(first_word) -> list:
    '''
    Функция, которая осуществляет поиск
    первого (единственного) компонента по базе данных
    '''

    if len(first_word) == 2:

        # print('Часть речи не указана')

        if first_word[1] == 'lemma':
            print(first_word[0])
            cur.execute(lemma_1, (first_word[0], ))
            res = cur.fetchall()

        if first_word[1] == 'word':
            cur.execute(word_1, (first_word[0], ))
            res = cur.fetchall()

        if first_word[1] == 'POS':
            cur.execute(pos_1, (first_word[0], ))
            res = cur.fetchall()

    if len(first_word) == 3 and '+POS' in first_word:

        # print('Часть речи указана')
        # print(first_word[0])

        if first_word[2] == 'lemma':
            cur.execute(
                lemma_pos_1,
                (first_word[0][0], first_word[0][1])
                )
            res = cur.fetchall()

        if first_word[2] == 'word':
            cur.execute(
                word_pos_1,
                (first_word[0][0], first_word[0][1])
                )
            res = cur.fetchall()

    return res


def search_2nd_word(second_word, text_id, new_id) -> list:
    '''
    Функция, которая осуществляет поиск
    второго (третьего) компонента по базе данных
    '''

    if len(second_word) == 2:

        # print('Часть речи не указана')

        if second_word[1] == 'lemma':
            cur.execute(
                lemma_2,
                (second_word[0], text_id, new_id)
                )
            res = cur.fetchone()

        if second_word[1] == 'word':
            cur.execute(
                word_2,
                (second_word[0], text_id, new_id)
                )
            res = cur.fetchone()

        if second_word[1] == 'POS':
            cur.execute(
                pos_2,
                (second_word[0], text_id, new_id)
                )
            res = cur.fetchone()

    if len(second_word) == 3 and '+POS' in second_word:

        # print('Часть речи указана')

        if second_word[2] == 'lemma':
            cur.execute(
                lemma_pos_2,
                (
                    second_word[0],
                    second_word[1],
                    text_id,
                    new_id
                    )
                )
            res = cur.fetchone()

        if second_word[2] == 'word':
            cur.execute(
                word_pos_2
                (
                    second_word[0],
                    second_word[1],
                    text_id,
                    new_id
                    )
                )
            res = cur.fetchone()

    print(res)

    return res


def main(req) -> list:
    '''
    Функция, которая осуществляет поиск
    введённых пользователем строк по базе данных.
    На вход принимается список из кортежей,
    в которых содержатся запрос и тип запроса
    '''

    # req - список кортежей (слово, тип)

    # длина запроса (1-3)
    len_query = len(req)

    # ищем комплексные запросы (вроде 'знать+NOUN')
    # разделяем и записываем их, как нам удобно
    # ставим отметку о том, что запрос содержит уточнение по тегу
    # это поможет распознать и применить нужный запрос
    new_req = []
    for tup in req:
        if '+' in tup[0]:  # прописать ошибку, если + найдётся в запросе-теге
            word_tag = tup[0].split('+')  # а если плюсов окажется несколько?
            content_type = (word_tag, '+pos', tup[1])
            new_req.append(content_type)
        else:
            new_req.append(tup)

    # print(new_req[0])

    if len_query == 1:

        # print('Длина запроса 1')
        results_list = []

        res_1 = search_1st_word(new_req[0])  # единый компонент запросов
        if res_1:
            for r in res_1:
                r_dict = {}
                r_dict['request'] = req[0][0]
                r_dict['sent'] = r[3]
                r_dict['link'] = r[4]
                results_list.append(r_dict)

    if len_query == 2:

        results_list = []  # выдача: список со словарями

        # ищем все подходящие 1ые компоненты
        # для каждого отдельного компонента
        # ищем 2ые компоненты в дополнение
        res_1 = search_1st_word(new_req[0])
        if res_1:
            req_text = req[0][0] + ' ' + req[1][0]
            for r in res_1:  # (id, text_id, sent_id, sent, link)
                text_id = r[1]  # text_id должен быть таким же
                new_id = r[0] + 1  # id токена по корпусу должен быть следующим
                r_2 = search_2nd_word(new_req[1], text_id, new_id)
                if r_2:
                    r_dict = {}  # выдача биграммы
                    r_dict['request'] = req_text
                    r_dict['sent'] = r[3]  # прописать 1 или 2 пр затрагивает запрос
                    r_dict['link'] = r[4]
                    results_list.append(r_dict)

    if len_query == 3:

        results_list = []  # выдача: список со словарями

        # ищем все подходящие 1ые компоненты
        # для каждого отдельного компонента
        # ищем 2ые компоненты в дополнение
        # для каждого отдельного 2го компонента
        # ищем третьи компоненты в дополнение
        res_1 = search_1st_word(new_req[0])
        if res_1:
            req_text = req[0][0] + ' ' + req[1][0] + ' ' + req[2][0]
            for r in res_1:
                text_id = r[1]  # text_id должен быть таким же
                new_id = r[0] + 1  # id токена по корпусу должен быть следующим
                r_2 = search_2nd_word(new_req[1], text_id, new_id)
                if r_2:
                    new_id_3 = r_2[0] + 1
                    r_3 = search_2nd_word(new_req[2], text_id, new_id_3)
                    if r_3:
                        r_dict = {}  # выдача триграммы
                        r_dict['request'] = req_text
                        r_dict['sent'] = r[3]  # прописать 1 или 2 пр затрагивает запрос
                        r_dict['link'] = r[4]
                        results_list.append(r_dict)

    return results_list


# print(main([('слушать', 'lemma')]))
# print(main([('что+PRON', 'lemma')]))
# print(main([('и', 'lemma'), ('вот', 'word')]))
# print(main([('PART', 'pos'), ('VERB', 'pos')]))
# print(main([('PART', 'pos'), ('быть', 'lemma'), ('NOUN', 'pos')]))
