from flask import flash, render_template, redirect, request
from flask_mail import Mail, Message
from app import app
from .forms import RequestForm

import uuid
import bdb_scraper

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def req():
    form = RequestForm()
    if form.validate_on_submit():
        return rec(form)
    return render_template('request.html', 
                           title='BDB-Scraper',
                           form=form)

def mail_url(email, url):
    msg = Message('Your BDB archive is ready',
                  sender = app.config['MAIL_USERNAME'],
                  recipients = [email])
    msg.body = "Here are your pictures: " + url
    mail.send(msg)
    pass

def rec(form):
    url = str(form['starturl'].data)
    email = str(form['email'].data)
    print(email)
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
    mail_url(email, request.url_root+zip_path+zip_name+'.zip')

    return render_template('done.html',
                           title='BDB-Scraper',
                           path=zip_path,
                           zipname=zip_name+'.zip')

