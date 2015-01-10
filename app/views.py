from app import app
from saltapi import SaltRestFul
from flask import render_template

s = SaltRestFul()

@app.route('/')
def index():
    grains = s.getGrains()

    return render_template('index.html',grains=grains)
@app.route('/run/<atgt>/<afun>/<aarg>')
def run(atgt,aarg,afun):
    result = s.Run(client='local',tgt=atgt,fun=afun,arg=aarg)
    return render_template('run.html',result=result)
