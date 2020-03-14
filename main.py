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


@app.route('/image_mars')
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


@app.route('/promotion_image')
def bootstrap():
    lst_of_promotion = ['Человечество вырастает из детства.',
                        'Человечеству мала одна планета.',
                        'Мы сделаем обитаемыми безжизненные пока планеты.',
                        'И начнем с Марса!',
                        'Присоединяйся!']
    list_of_alerts = ['success', 'info', 'warning', 'danger', 'primary']

    return ('''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{}" alt="здесь должна была быть картинка, но не нашлась">
                    '''.format(url_for('static', filename='css/style.css'),
                               url_for('static', filename='image/mars.png')) +
            ''.join(['<div class="alert alert-' + list_of_alerts[i]
                     + '" role="alert">' + lst_of_promotion[i] + '</div>' for i in range(len(lst_of_promotion))])
            + '''</body> 
     </html>''')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
