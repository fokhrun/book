
import os
from flask import Flask
from book_app import create_app


app = create_app("default")


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
