#!/usr/bin/env python3
"""basic babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """babel config class"""
    LANGUAGES = ['en',
                 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """babel local selector func"""
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', strict_slashes=False)
def index():
    """display “Hello world”"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
