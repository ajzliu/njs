from flask import (Flask, render_template, redirect, abort, 
                   url_for, request, make_response, session, make_response)
from numberjumble import evaluate

app = Flask(__name__)
app.config['SECRET_KEY'] = b'qA9#J[^JAK9&{YATBWVG4&W-|!CF'

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "egan" and password == "eganshowcase2019":
            session['username'] = username
            return redirect(url_for('landing'))
        else:
            return render_template('index.html', response = "Incorrect Password")
    elif 'username' in session:
        return '''
        <!doctype html>
        <header>
            <title>Number Jumble Solver</title>
            <style>
                html * {
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, sans-serif !important;
                }
                body {
                    margin-left: 15px;
                    text-align: center;
                }
                .logout {
                    position:absolute; 
                    top:0; 
                    right:0;
                }
            </style>
        </header>
        <body>
            <form action="/logout" class="logout">
                <input type="submit" value="Log Out">
            </form>
            <a href="/landing">Enter Number Jumble</a>
            <br/>
            <a href="/submitted">View Solution</a>
        </body>
        '''
    return render_template('index.html', response = "")

@app.route("/landing", methods=['GET'])
def landing():
    if 'username' in session:
        return render_template('landing.html')
    else:
        abort(401)

@app.route("/evaluate", methods=['POST'])
def runprocessing():
    if 'username' in session:
        numbers = [int(x) for x in request.form.getlist('n')]
        ops = [x for x, y in request.form.items() if y == 'on']
        evaluate(
            numbers, 
            int(request.form.get('target')), 
            float(request.form.get('extcalc')), 
            ops)
        return redirect(url_for('submitted'))
    else:
        abort(401)

@app.route("/submitted", methods=['GET'])
def submitted():
    if 'username' in session:
        with open('snj.txt','r') as f:
            text = f.read()
        resp = make_response(render_template('submitted.html', text = text))
        resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        resp.headers["Pragma"] = "no-cache"
        resp.headers["Expires"] = "0"
        return resp
    else:
        abort(401)

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
