from flask import Flask, render_template

app = Flask(__name__)
app.config.update(logged=1)

posts = ["One", "Two", "Three"]


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', is_authorized=True, posts=posts)


@app.route('/signin.html')
def signin():
    return render_template('signin.html')


@app.route('/login.html')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=1)
