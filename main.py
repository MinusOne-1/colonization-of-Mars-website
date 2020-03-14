from flask import Flask, url_for

app = Flask(__name__)

way = 'http://127.0.0.1:8080/'


@app.route('/')
def default():
    return '''<h1>Миссия Колонизация Марса</h1>'''


@app.route('/index')
def index():
    return '<div><h1>И на Марсе будут яблони цвести!</h1></div>'


@app.route('/promotion')
def promotion():
    return '''Человечество вырастает из детства. <br><br>
Человечеству мала одна планета.<br><br>
Мы сделаем обитаемыми безжизненные пока планеты.<br><br>
И начнем с Марса!<br><br>
Присоединяйся!'''


@app.route('/image_sample')
def image():
    return ("""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>""" +
            '''<h1>Жди нас, Марс!</h1>
                <img src="{}" alt="здесь должна была быть картинка, 
                но не нашлась">'''.format(url_for('static', filename='image/mars.png')) +
            """"<div>Планета Марс во всей красе</div>
                </body>
          </html>""")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
