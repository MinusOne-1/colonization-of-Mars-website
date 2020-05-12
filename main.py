from flask import Flask, render_template, url_for

from data.Jobs import Jobs
from data.db_session import global_init, create_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def show_orders_db():
    session = create_session()
    res = [[str(i.id), str(i.job), str(i.user.name + ' ' + i.user.surname),
            str(i.work_size), str(i.collaborators),
            str(i.is_finished)] for i in session.query(Jobs).all()]
    return res


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['title'] = 'Заготовка'
    return render_template('base.html', **param)


@app.route('/jobs')
def all_order_func():
    param = {}
    param['title'] = 'Работа'
    param['orders'] = show_orders_db()
    print(param['orders'])
    param['len_orders'] = len(param['orders'])
    return render_template('jobs.html', **param)


@app.route('/training/<prof>')
def specialty_simulator(prof):
    param = {}
    param['specialty'] = prof
    param['inj_image'] = url_for('static', filename='image/inj_image.png')
    param['sci_image'] = url_for('static', filename='image/sci_image.png')
    return render_template('specialty_simulator.html', **param)


@app.route('/list_prof/<list>')
def list_prof(list):
    param = {}
    param['specialtys'] = ['Инженер-исследователь', "пилот", "врач", "строитель", "экзобиолог", "климатолог"]
    param['lst_type'] = list
    return render_template('list_prof.html', **param)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    param = {}
    param['title'] = 'Анкета'
    param['surname'] = 'Watny'
    param['name'] = 'Mark'
    param['education'] = 'выше среднего'
    param['profession'] = 'штурман марсохода'
    param['sex'] = 'male'
    param['motivation'] = 'Всегда мечтал застрять на Марсе!'
    param['ready'] = 'True'

    return render_template('auto_answer.html', **param)


if __name__ == '__main__':
    global_init('db/db.sqlite')
    app.run(port=8080, host='127.0.0.1')
