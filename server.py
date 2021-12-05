from flask import Flask, render_template,request,redirect,session,sessions

app = Flask(__name__)
app.secret_key = 'bofa'

@app.route('/')
def index():
    return render_template("form.html")

@app.post('/result')
def result():
    name = request.form['name']
    dojo_loc = request.form['dojo_loc']
    fav_lang = request.form['fav_lang']
    comments = request.form['comments']
    return render_template('result.html', name=name, dojo_loc=dojo_loc, fav_lang=fav_lang, comments=comments)

if __name__ == "__main__":
    app.run(debug=True)
