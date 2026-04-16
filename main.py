#!/usr/bin/env python

from collections import defaultdict
import logging
import flask
import os

log = logging.getLogger(__name__)

app = flask.Flask(__name__)

SERIES_COUNT_DICT = defaultdict(str)
SERIES_COUNT_DICT['golf'] = ('golf', 5)
SERIES_COUNT_DICT['waterscapes'] = ('wat', 8)
SERIES_COUNT_DICT['landscapes'] = ('land', 14)
SERIES_COUNT_DICT['poms'] = ('pom', 4)
SERIES_COUNT_DICT['skyscrapers'] = ('sky', 2)
SERIES_COUNT_DICT['textures'] = ('tex', 6)
SERIES_COUNT_DICT['main'] = ('main', 9)

SERIES_COUNT_DICT['light'] = ('light', 6)
SERIES_COUNT_DICT['textures2'] = ('tex', 20)

@app.route("/")
@app.route("/home")
def home():
    return flask.render_template('home.html')

@app.route("/about_artist")
def about_artist():
    return flask.render_template('about_artist.html')

@app.route("/statement_bio")
def statement_bio():
    return flask.render_template('statement_bio.html')

@app.route("/resume")
def resume():
    return flask.render_template('resume.html')

@app.route("/contact")
def contact():
    return flask.render_template('contact.html')

@app.route("/portfolio")
def portfolio():
    return flask.render_template('portfolio.html')

@app.route("/portfolio/texture")
def folio_textures():
    series = 'textures2'
    pic_text =""
    
    return flask.render_template('folio_textures.html', series=series, pic_text=pic_text, bname=SERIES_COUNT_DICT[series][0], count=SERIES_COUNT_DICT[series][1])

@app.route("/portfolio/<series>")
def folio_series(series):
    if series not in SERIES_COUNT_DICT:
        flask.abort(404)

    text_fn = os.path.join("static", "images", series, "series.htm")
    try:
        with open(text_fn) as fd:
            pic_text = fd.read()
    except FileNotFoundError:
        pic_text = ""
        
    return flask.render_template('folio_series.html', series=series, pic_text=pic_text, bname=SERIES_COUNT_DICT[series][0], count=SERIES_COUNT_DICT[series][1])

@app.route("/portfolio/view_single/<series>/<bname>/<int:pn>")
def folio_view_single(series, bname, pn):
    if series not in SERIES_COUNT_DICT:
        flask.abort(404)
        
    max_count = SERIES_COUNT_DICT[series][1]

    if pn <= 0:
        pn = 1
    elif pn > max_count:
        pn = max_count

    text_fn = os.path.join("static", "images", series, f"{bname}{pn}.htm")
    try:
        with open(text_fn) as fd:
            pic_text = fd.read()
    except FileNotFoundError:
        pic_text = ""
        
    return flask.render_template('folio_view_single.html', series=series, bname=bname, pn=pn, pic_text=pic_text)


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
