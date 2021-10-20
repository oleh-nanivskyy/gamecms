from flask import Blueprint

from app.database import get_db 

bp = Blueprint('v1', __name__, url_prefix='/v1')


@bp.route('/ver')
def index():
    conn = get_db()
    with conn.cursor() as cur:
        cur.execute('SELECT version()')
        ver = cur.fetchone()
        return ver[0]