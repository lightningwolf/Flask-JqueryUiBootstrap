#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.jqueryuibootstrap import JqueryUiBootstrap

app = Flask(__name__)
JqueryUiBootstrap(app)


@app.route('/')
def index():
    return render_template('noforms.html')


@app.route('/breakme/')
def breakme():
    return render_template('noformserror.html')


if __name__ == '__main__':
    app.run(debug=True)
