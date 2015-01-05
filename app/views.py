from app import app
from flask import render_template,request
import json
from forms import *
from app import saltclient

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/data')
def data():
    obj={'name':"aa",'youjianyingxiao':'[120, 132, 101, 134, 90000, 230, 210]'}
    return json.dumps(obj)
@app.route('/form')
def form():
    form = MyForm()
    return render_template('submit.html',form=form)
@app.route('/bootstrap')
def bootstrap():
    return render_template("bootstrap.html")

@app.route('/login')
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            nickname = form.data['nickname']
            psdmd5 = md5(form.data['password'])
            password = psdmd5.hexdigest()
            remember_me = form.data['remember_me']
            user = User.query.filter_by(
                nickname=nickname, password=password).first()
            if user:
                login_user(user, remember=remember_me)
                flash('signin successful')
                return redirect(request.args.get("next") or url_for("index"))
            else:
                flash('try again')
    return render_template('forms/login.html', form = form)

@app.route('/about')
def about():
    ret=saltclient.cmd('SC','cmd.run',['df -h',])
    return render_template('pages/placeholder.about.html',ret=ret)

@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form = form)

@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form = form)
