from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['title'] = 'Заготовка'
    return render_template('base.html', **param)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
