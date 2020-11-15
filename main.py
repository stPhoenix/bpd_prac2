#-*- coding: utf8 -*-

from flask import Flask, request, render_template
import sqlite3
from random import randint

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {'error': False, 'message': None, 'data': None}
    cursor = sqlite3.connect('db.sqlite3')
    imgs = cursor.execute('SELECT * FROM Imgs').fetchall()
    img = imgs[randint(0, len(imgs)-1)]

    result['data'] = {'img': img[1], 'id': img[0]}
    if request.method == 'GET':
        return render_template('index.html', name='index', result=result)
    else:
        try:
            answer = request.form['answer']
            ids = int(request.form['id'])
            fromdb = cursor.execute('SELECT CODE FROM Imgs WHERE ID=? ;', (ids, )).fetchone()

            result['data']['answer'] = 'Correct' if (answer == fromdb[0]) else 'Incorrent'
        except Exception as e:
            result['action'] = ''
            result['error'] = True
            result['message'] = e
        return render_template('index.html', name='index', result=result)