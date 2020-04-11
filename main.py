from flask import Flask, url_for, request
import os

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


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <div>
                                <h1>Анкета претендента</h1>
                            </div>
                            <div>
                                <h3>на участие в миссии</h3>
                            </div>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Фамилия" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Имя" name="name">
                                    <br>

                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <br>
                                        <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="obrazSelect" name="obraz">
                                          <option>Начальное</option>
                                          <option>Неполное среднее</option>
                                          <option>Полное среднее</option>
                                          <option>Высшее</option>
                                          <option>Несколько высших</option>
                                        </select>
                                     </div><br>

                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="reason" rows="5" name="reason"></textarea>
                                    </div><br>

                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                    </div>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    <br>

                                   <div class="form-group form-check">
                                       <label>Какая у вас профессия?</label>
                                        <br>

                                        <input type="checkbox" class="form-check-input" id="sercher" name="ing-sercher">
                                        <label class="form-check-label" for="sercher">Инженер-исследователь</label>
                                        <br>

                                        <input type="checkbox" class="form-check-input" id="builder" name="ing-builder">
                                        <label class="form-check-label" for="builder">Инженер-строитель</label>
                                        <br>

                                        <input type="checkbox" class="form-check-input" id="pilot" name="pilot">
                                        <label class="form-check-label" for="pilot">Пилот</label>
                                        <br>

                                        <input type="checkbox" class="form-check-input" id="temperateman" name="temperateman">
                                        <label class="form-check-label" for="temperateman">Метеоролог</label>
                                        <br>

                                        <input type="checkbox" class="form-check-input" id="life" name="ing-life">
                                        <label class="form-check-label" for="life">Инженер по жизнеобеспечению</label>
                                        <br>

                                        <input type="checkbox" class="form-check-input" id="radiation" name="ing-radiation-def">
                                        <label class="form-check-label" for="radiation">Инженер по радиационной защите</label>
                                        <br>

                                        <input type="checkbox" class="form-check-input" id="doctor" name="doctor">
                                        <label class="form-check-label" for="doctor">Врач</label>
                                        <br>

                                        <input type="checkbox" class="form-check-input" id="biolog" name="biolog">
                                        <label class="form-check-label" for="biolog">Экзобиолог</label>
                                    </div>
                                    <br>
                                    
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['obraz'])
        print(request.form['file'])
        print(request.form['reason'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def greeting(planet_name):
    lst_of_promotion = ['На ней много необходимых ресурсов;',
                        'На ней есть вода и атмосфера;',
                        'На ней есть небольшое магнитное поле;',
                        'Наконец, она просто красива!']
    list_of_alerts = ['success', 'info', 'warning', 'danger']
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                   integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                   crossorigin="anonymous">
                    <title>Вариант выбора</title>
                  </head>
                  <body>
                    <h1>Моё предложение: {}</h1>
                    <h3>Эта планета близка к Земле;</h3>'''.format(planet_name) + \
           ''.join(['<div class="alert alert-' + list_of_alerts[i]
                    + '" role="alert">' + lst_of_promotion[i] + '</div>' for i in range(len(lst_of_promotion))]) + '''
                  </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def res_of_otbor(nickname, level, rating):
    lst_of_promotion = ['Поздравляем! Ваш рейтинг после {} этапа отбора составляет {}!',
                        'Желаем удачи!']
    list_of_alerts = ['success', 'warning']
    return ('''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                   integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                   crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                  <h1>Результаты отбора</h1>
                    <h3>Претендент на участие в миссии {}:</h3>''' +
            ''.join(['<div class="alert alert-' + list_of_alerts[i]
                     + '" role="alert">' + lst_of_promotion[i] + '</div>' for i in range(len(lst_of_promotion))]) + '''
                  </body>
                </html>''').format(nickname, level, rating)

file = 'Файл не выбран'
@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo_form():
    global file

    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <form method="post" enctype="multipart/form-data">
                            <div>
                                <h1>Загрузка фотографии</h1>
                            </div>
                            <div>
                                <h3>для участия в миссии</h3>
                            </div>
                            <div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                    </div>
                                        <input type="file" class="form-control-file" id="file" name="file">
                                       <label>{file}</label>
                                    <br>
                                    <img src="{file}" alt="здесь должна была быть картинка, но не нашлась">
                                      <br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file'].read()
        image_ = open('static/image/img.png', 'wb')
        image_.write(f)
        image_.close()
        file = 'static/image/img.png'
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <form method="post" enctype="multipart/form-data">
                            <div>
                                <h1>Загрузка фотографии</h1>
                            </div>
                            <div>
                                <h3>для участия в миссии</h3>
                            </div>
                            <div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                    </div>
                                        <input type="file" class="form-control-file" id="file" name="file">
                                       <label>{file}</label>
                                    <br>
                                    <img src="{file}" alt="здесь должна была быть картинка, но не нашлась">
                                      <br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''

@app.route('/carousel')
def carousel():
    lst = [('static/image/mars1.jpg', '...'),
           ('static/image/mars2.jpg', '...'), ('static/image/mars3.jpg', '...'), ('static/image/mars4.jpg', '...'),
           ('static/image/mars5.jpg', '...')]
    return ('''<!DOCTYPE html>
<html lang="en">
<head>
  <title>Пейзажи Марса</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>
  <style>
      h1 {
      margin:0 45% 0 40%;
      width:50%;
        color: #d22e3a
      }
  /* Make the image fully responsive */
      .carousel-inner img {
          width: 100%;
          height: 100%;
      }
  </style>
</head>
<body>
<h1>Пейзажи Марса</h1>
<br>
<div id="demo" class="carousel slide" data-ride="carousel">

  <!-- Indicators -->
  <ul class="carousel-indicators">
    <li data-target="#demo" data-slide-to="0" class="active"></li>
    <li data-target="#demo" data-slide-to="1"></li>
    <li data-target="#demo" data-slide-to="2"></li>
    <li data-target="#demo" data-slide-to="3"></li>
    <li data-target="#demo" data-slide-to="4"></li>
  </ul>
  
  <!-- The slideshow -->
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="''' + lst[0][0] +'''" alt="''' + lst[0][1] +'''" width="2000" height="2000">
    </div>''' + ''.join([f'''<div class="carousel-item">
      <img src="{i[0]}" alt="{i[1]}" width="2000" height="2000">
    </div>''' for i in lst[1:]])
    + '''
  </div>
  
  <!-- Left and right controls -->
  <a class="carousel-control-prev" href="#demo" data-slide="prev">
    <span class="carousel-control-prev-icon"></span>
  </a>
  <a class="carousel-control-next" href="#demo" data-slide="next">
    <span class="carousel-control-next-icon"></span>
  </a>
</div>

</body>
</html>
''')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
