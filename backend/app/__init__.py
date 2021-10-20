from flask import Flask, url_for, redirect

app = Flask(__name__, subdomain_matching=True)


@app.route('/')
def hello():
    return redirect(url_for('v1.index'))

from app.api import bp
app.register_blueprint(bp)

from app.database import close_db
app.teardown_appcontext(close_db)