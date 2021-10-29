import os

from flask import Flask, url_for, redirect

HOST = os.environ.get('POSTGRES_HOST')
DB_NAME = os.environ.get('POSTGRES_DB')
USER = os.environ.get('POSTGRES_USER')
PASSWORD = os.environ.get('POSTGRES_PASSWORD')

app = Flask(__name__, subdomain_matching=True)
app.config["SQLALCHEMY_DATABASE_URI"] = \
    f"postgresql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}"


@app.route('/')
def hello():
    return redirect(url_for('v1.index'))


from app.api import bp
app.register_blueprint(bp)