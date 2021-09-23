from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/play', methods=['GET'])
def principal():
    num = 3
    return render_template('index.html', num=num)


@app.route('/play/<num>', methods=['GET'])
def play(num):

    return render_template('index.html', num=int(num))


@app.route('/play/<num>/<color>', methods=['GET'])
def color(num, color):
    return render_template('index.html', num=int(num), color=color)


if __name__ == "__main__":
    app.run(debug=True)
