from flask import Blueprint, jsonify

from app.database import get_db 

bp = Blueprint('v1', __name__, url_prefix='/v1')


@bp.route('/')
def index():
    return "Hello, World. It is game-cms api V1."
    # conn = get_db()
    # with conn.cursor() as cur:
    #     cur.execute('SELECT version()')
    #     ver = cur.fetchone()
    #     return ver[0]


@bp.route('/companies')
def companies():
    conn = get_db()
    with conn.cursor() as cur:
        cur.execute('''
            SELECT company_id, name, foundation_date
            FROM companies
        ''')
        return jsonify(cur.fetchall())