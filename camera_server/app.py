from flask import Flask, render_template

_PATH = '../video_cap/resources/trained_models/haarcascade_frontalface_default.xml'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/configure')
def configure():
    return render_template('configuration.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')