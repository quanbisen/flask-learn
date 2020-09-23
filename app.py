
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test', methods=['GET', 'POST'])
def print_test():
    if request.method == 'POST':
        number1 = request.form['number1']
        number2 = request.form['number2']
        number3 = int(number1) + int(number2)
        print(request.headers.get('user-agent'))
        return render_template('test.html', message=str(number3))
    return render_template('test.html', message='Backend message')


@app.route('/user/<username>', methods=['GET'])
def show_user_profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>', methods=['GET'])
def show_post_id(post_id):
    return 'Post %d' % post_id


@app.route('/path/<path:sub_path>', methods=['GET'])
def show_sub_path(sub_path):
    return 'Path %s' % sub_path


if __name__ == '__main__':
    app.run(port=8080)
