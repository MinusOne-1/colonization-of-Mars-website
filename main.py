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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
