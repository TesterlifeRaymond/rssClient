# -*- coding: utf-8 -*-
"""
    webapi.app
    ~~~~~~~~~~

    DESCRIPTION

    :copyright: (c) 2018 by  Raymond.
    :last modified by 2018-09-12 16:56:31
"""

from flask import Flask, abort, request
import os

app = Flask(__name__)


@app.route("/rss/<tag>")
def index(tag):
    print(tag)
    if tag in os.listdir("rss_xml"):
        return open("rss_xml/{}".format(tag)).read()
    return abort(404)


if __name__ == "__main__":
    app.run()
