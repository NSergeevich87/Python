from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "<h1>КСЮНЯ БОЛЬШАЯ СВИНКА!</h1><br><a href='/index'>НАЖМИ СЮДА ЖАБУНЬ!</a>"

@app.route('/index')
def index():
    return "<h1>А НИКИТА ГИГАНТСКИЙ ХАБАЛИТО!</h1>"

if __name__ == '__main__':
    app.run()