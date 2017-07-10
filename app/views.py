from flask import flash, render_template, redirect
from app import app
from .forms import RequestForm

import uuid
from bdb_scraper import bdb_scraper

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

    name = bdb_scraper.zip_name_from_url(url) + '-' + uuid.uuid4().hex
    zip_path = "static/zips/"
    zip_name = name

    bdb_scraper.scrape(url,
                       username=username, password=password,
                       save_text=save_text,
                       create_zip=True,
                       zip_name='app/'+zip_path+zip_name,
                       zip_base='files/',
                       dest="files/"+name)

    return render_template('done.html',
                           title='BDB-Scraper',
                           path=zip_path,
                           zipname=zip_name+'.zip')

