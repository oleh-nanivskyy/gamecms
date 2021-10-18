from flask import Flask

app = Flask(__name__, subdomain_matching=True)
app.config['SERVER_NAME'] = 'localhost:5000'

from app.api import bp
app.register_blueprint(bp)

from app.database import close_db
app.teardown_appcontext(close_db)