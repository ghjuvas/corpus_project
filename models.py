from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
import sqlite3

db = SQLAlchemy()

con = sqlite3.connect('anecdotes.db')
cur = con.cursor()


# так можно создать штуки, которые потом пойдут в нашу html
# сохранение поисковых запросов?
# class Request(db.Model):

#     __tablename__ = 'corpora'  # туть название таблицы откуда берется инфа

#     req_id = db.Column(
#         'id', db.Integer,
#         primary_key=True,
#         autoincrement=True)
#     input1 = db.Column('input1', db.Text)
#     input2 = db.Column('input2', db.Text)
#     input3 = db.Column('input3', db.Text)


class Metainformation(db.Model):

    __tablename__ = 'texts_meta'

    id = db.Column(
        'id', db.Integer,
        primary_key=True,
        autoincrement=True)
    vk_id = db.Column('vk_id', db.Text)
    text = db.Column('text', db.Text)
    link = db.Column('link', db.Text)


class Words(db.Model):

    __tablename__ = 'morph_parse'

    token_id = db.Column(
        'id', db.Integer,
        primary_key=True,
        autoincrement=True)
    text_id = db.Column('text_id', db.Integer)
    token = db.Column('token', db.Text)
    lemma = db.Column('lemma', db.Text)
    pos = db.Column('POS', db.Text)


class Sentences(db.Model):

    __tablename__ = 'sents'

    id = db.Column(
        'id', db.Integer,
        primary_key=True,
        autoincrement=True)
    text_id = db.Column('text_id', db.Integer)
    sent_id = db.Column('sent_id', db.Integer)
    sent = db.Column('sent', db.Text)
