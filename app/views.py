from flask import flash, render_template, redirect
from app import app
from .forms import RequestForm

import bdb_scraper

#@app.route('/')
#@app.route('/derp')
#def derp():
#    return "Hello world"

@app.route('/', methods=['GET', 'POST'])
def request():
    form = RequestForm()
    if form.validate_on_submit():
        return rec(form)
    return render_template('request.html', 
                           title='BDB-Scraper',
                           form=form)

def rec(form):
    url = str(form['stringurl'].data)
    #email = str(form['email'].data)
    username = str(form['username'].data)
    password = str(form['password'].data)
    save_text = form['save_text'].data
    bdb_scraper.scrape(url)
    return ("received data:"
            + "<br>url: " + url
            + "<br>username:" + username
            + "<br>password" + password
            + "<br>save_text: " + str(save_text))
    # render_template('received.html',
    #                  title="Request received")

