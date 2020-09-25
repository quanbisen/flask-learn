from html import escape

from flask import Flask, url_for
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


@app.route('/directory', methods=['GET'])
def directory():
    return render_template('directory/index.html')


@app.route('/user/<username>', methods=['GET'])
def show_user_profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>', methods=['GET'])
def show_post_id(post_id):
    return 'Post %d' % post_id


@app.route('/path/<path:sub_path>', methods=['GET'])
def show_sub_path(sub_path):
    return 'Path %s' % sub_path


@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    return '1'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', name='lollipop'))
#     print(url_for('profile', username='John Doe'))


with app.test_request_context('/login', method='GET'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/login'
    assert request.method == 'GET'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload-test.html')
    elif request.method == 'POST':
        file = request.files['file']
        file.save('/var/www/test.txt')
        return 'upload success.'


if __name__ == '__main__':
    app.run(port=8080)
