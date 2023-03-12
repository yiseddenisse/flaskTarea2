from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username[0].isupper() and password.isalnum():
            return redirect(url_for('login_successful'))
        else:
            return redirect(url_for('login'))
    return render_template('index.html')


@app.route('/success')
def login_successful():
    return 'Has ingresado correctamente'



if __name__ == '__main__':
    app.run()
