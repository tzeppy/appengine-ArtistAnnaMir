#!/usr/bin/env python

from collections import defaultdict
import logging
import flask
import os

log = logging.getLogger(__name__)

app = flask.Flask(__name__)

seriesCountDict = defaultdict(int)
seriesCountDict['golf'] = ('golf', 5)
seriesCountDict['waterscapes'] = ('wat', 8)
seriesCountDict['landscapes'] = ('land', 14)
seriesCountDict['poms'] = ('pom', 4)
seriesCountDict['skyscrapers'] = ('sky', 2)
seriesCountDict['textures'] = ('tex', 6)
seriesCountDict['main'] = ('main', 9)

seriesCountDict['light'] = ('light', 6)
seriesCountDict['textures2'] = ('tex', 20)

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
    global seriesCountDict
    series = 'textures2'
    pic_text =""
    
    return flask.render_template('folio_textures.html', series=series, pic_text=pic_text, bname=seriesCountDict[series][0], count=seriesCountDict[series][1])

@app.route("/portfolio/<series>")
def folio_series(series):
    global seriesCountDict

    text_fn = "static/images/%s/series.htm" % series
    if os.path.exists(text_fn):
        with open(text_fn) as fd:
            pic_text = fd.read()
    else:
        pic_text = ""
    return flask.render_template('folio_series.html', series=series, pic_text=pic_text, bname=seriesCountDict[series][0], count=seriesCountDict[series][1])

@app.route("/portfolio/view_single/<series>/<bname>/<int:pn>")
def folio_view_single(series, bname, pn):
    global seriesCountDict

    if pn <= 0:
        pn = 1
    elif pn > seriesCountDict[series][1]:
        pn = seriesCountDict[series][1]

    text_fn = "static/images/%s/%s%s.htm" % (series, bname, pn)
    if os.path.exists(text_fn):
        with open(text_fn) as fd:
            pic_text = fd.read()
    else:
        pic_text = ""
    return flask.render_template('folio_view_single.html', series=series, bname=bname, pn=pn, pic_text=pic_text)


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
