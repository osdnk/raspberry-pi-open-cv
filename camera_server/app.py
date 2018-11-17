from flask import Flask, render_template, request
import configparser
_PATH = '../video_cap/resources/trained_models/haarcascade_frontalface_default.xml'
_CONFIG_PATH = 'config.ini'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

def save_config(request):
    config = configparser.ConfigParser()
    config.add_section('email')
    config.set('email', 'server', request.form['server'])
    config.set('email', 'port', request.form['port'])
    config.set('email', 'username', request.form['username'])
    config.set('email', 'password', request.form['password'])
    config.set('email', 'fromaddr', request.form['fromaddr'])
    config.set('email', 'toaddr', request.form['toaddr'])
    with open(_CONFIG_PATH, 'w') as configfile:
        config.write(configfile)

@app.route('/configure', methods=['GET', 'POST'])
def configure():
    if request.method == 'POST':
        save_config(request)
        return "Config saved"
    return render_template('configuration.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')