from flask import Blueprint, jsonify

from app.models import Users, Companies, Games, Reviews, Screenshots

bp = Blueprint('v1', __name__, url_prefix='/v1')


@bp.route('/')
def index():
    return 'Hello, World. It is game-cms api V1.'


@bp.route('/companies')
def get_companies():
    companies_data = Companies.query.all()
    
    formatted = []
    for c in companies_data:
        formatted.append(
            {
                'companyID': c.company_id,
                'title': c.name,
                'date': str(c.foundation_date)
            }
        )

    return jsonify(formatted)