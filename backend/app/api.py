from datetime import datetime

from flask import Blueprint
from flask_restful import Resource, Api, reqparse, abort

from app.models import db, Users, Companies, Games, Reviews, Screenshots

bp = Blueprint('v1', __name__)
api = Api(bp)

parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('description', type=str)
parser.add_argument('text', type=str)
parser.add_argument('ceo', type=str)
parser.add_argument('date', type=str)
parser.add_argument('companyId', type=int)
parser.add_argument('gameId', type=int)
parser.add_argument('rating', type=int)


class CompaniesList(Resource):
    def get(self):
        companies_list = Companies.query.all()
    
        formatted = []
        for c in companies_list:
            formatted.append({
                    'companyId': c.company_id,
                    'title': c.name,
                    'date': str(c.foundation_date)
                })

        return formatted

    def post(self):
        args = parser.parse_args()

        new_company = Companies(name=args['title'], 
                                ceo=args['ceo'],
                                description=args['description'],
                                foundation_date=args['date'])

        db.session.add(new_company)
        db.session.commit()

        return new_company.company_id, 201


class CompaniesID(Resource):
    def get(self, company_id):
        company = Companies.query.get(company_id)
        
        if not company:
            abort(404, message=f"Company id {company_id} does not exist.")
        
        formatted = {
            "companyId": company.company_id,
            "title": company.name,
            "ceo": company.ceo,
            "date": str(company.foundation_date)
        }

        return formatted

    def put(self, company_id):
        code = None
        args = parser.parse_args()

        old_company = Companies.query.get(company_id);
        
        if not old_company:
            new_company = Companies(company_id=company_id,
                                    name=args['title'], 
                                    ceo=args['ceo'],
                                    description=args['description'],
                                    foundation_date=args['date'])
            db.session.add(new_company)
            code = 201
        else:
            old_company.name = args['title']
            old_company.description = args['description']
            old_company.foundation_date = args['date']
            old_company.ceo = args['ceo']

            code = 204           

        db.session.commit()

        return '', code

    def delete(self, company_id):
        company = Companies.query.get(company_id)
        
        if not company:
            abort(404, message=f"Company id {company_id} does not exist.")

        db.session.delete(company)
        db.session.commit()

        return '', 204        


class GamesList(Resource):
    def get(self):
        games_list = Games.query.all()
    
        formatted = []
        for g in games_list:
            formatted.append({
                'gameId': g.game_id,
                'title': g.name,
                'company': g.companies.name,
                'date': str(g.release_date)
            })

        return formatted

    def post(self):
        args = parser.parse_args()
        
        game = Games(company_id=args['companyId'],
                     name=args['title'],
                     description=args['description'],
                     release_date=args['date'])

        db.session.add(game)
        db.session.commit()

        return game.game_id, 201


class GamesID(Resource):
    def get(self, game_id):
        game = Games.query.get(game_id)
    
        if not game:
            abort(404, message=f"Game id {game_id} does not exist.")

        formatted = {
            "gameId": game.game_id,
            "companyId": game.company_id,
            "title": game.name,
            "date": str(game.release_date),
            "description": game.description,
            "rating": None if len(game.reviews) == 0 else round(
                sum(r.rating for r in game.reviews) / len(game.reviews), 1)
        }

        return formatted

    def put(self, game_id):
        code = None
        args = parser.parse_args()

        old_game = Games.query.get(game_id);
        
        if not old_game:
            new_game = Games(game_id=game_id,
                             company_id=args['companyId'], 
                             name=args['title'],
                             description=args['description'],
                             release_date=args['date'])
            db.session.add(new_game)
            code = 201
        else:
            old_game.company_id = args['companyId']
            old_game.name = args['title']
            old_game.description = args['description']
            old_game.release_date = args['date']

            code = 204           

        db.session.commit()

        return '', code

    def delete(self, game_id):
        game = Games.query.get(game_id)
    
        if not game:
            abort(404, message=f"Game id {game_id} does not exist.")

        db.session.delete(game)
        db.session.commit()

        return '', 204


class CompaniesIDGamesList(Resource):
    def get(self, company_id):
        company = Companies.query.get(company_id)
        
        if not company:
            abort(404, message=f"Company id {company_id} does not exist.")
        
        formatted = []
        for game in company.games:
            formatted.append({
                "gameId": game.game_id,
                "title": game.name,
                "rating": None if len(game.reviews) == 0 else round(
                    sum(r.rating for r in game.reviews) / len(game.reviews), 1)
            })

        return formatted

    def post(self, company_id):
        args = parser.parse_args()

        if not Companies.query.get(company_id):
            abort(404, message=f"Company id {company_id} does not exist.")
        
        game = Games(company_id=company_id,
                     name=args['title'],
                     description=args['description'],
                     release_date=args['date'])

        db.session.add(game)
        db.session.commit()

        return game.game_id, 201


class GamesIDThumbnailsList(Resource):
    def get(self, game_id):
        game = Games.query.get(game_id)
        
        if not game:
            abort(404, message=f"Game id {game_id} does not exist.")
        
        formatted = []
        for screenshot in game.screenshots:
            formatted.append({
                "scrennshotId": screenshot.screenshot_id,
                "thumbnailName": screenshot.thumbnail_name
            })

        return formatted


class ScreenshotsID(Resource):
    def get(self, screenshot_id):
        screenshot = Screenshots.query.get(screenshot_id)
    
        if not screenshot:
            abort(404, message=f'Screenshot id {screenshot_id} does not exist.')

        return screenshot.file_name


class GamesIDReviewsList(Resource):
    def get(self, game_id):
        game = Games.query.get(game_id)

        if not game:
            abort(404, message=f'Game id {game_id} does not exist.')
    
        formatted = []
        for r in game.reviews:
            formatted.append(
                {
                    "reviewId": r.review_id,
                    "username": r.users.login,
                    "text": r.content,
                    "rating": r.rating
                }
            )

        return formatted


class UserIDReviewsList(Resource):
    def get(self, user_id):
        user = Users.query.get(user_id)

        if not user:
            abort(404, message=f'User id {user_id} does not exist.')
    
        formatted = []
        for r in user.reviews:
            formatted.append(
                {
                    "reviewId": r.review_id,
                    "gameTitle": r.games.name,
                    "text": r.content,
                    "rating": r.rating
                }
            )

        return formatted

    def post(self, user_id):
        args = parser.parse_args()

        if not Users.query.get(user_id):
            abort(404, message=f'User id {user_id} does not exist.')

        review = Reviews(game_id=args['gameId'],
                         user_id=user_id,
                         content=args['text'],
                         rating=args['rating'],
                         creation_date=datetime.now().strftime('%Y-%m-%d'))

        db.session.add(review)
        db.session.commit()

        return review.review_id, 201


class ReviewsID(Resource):
    def delete(self, review_id):
        review = Reviews.query.get(review_id)

        if not review:
            abort(404, message=f'Review id {review_id} does not exist.')

        db.session.delete(review)
        db.session.commit()

        return '', 204

    def patch(self, review_id):
        args = parser.parse_args()
        review = Reviews.query.get(review_id)

        if not review:
            abort(404, message=f'Review id {review_id} does not exist.')

        review.content = args['text'] or review.content
        review.rating = args['rating'] or review.rating

        db.session.commit()

        return '', 204


api.add_resource(CompaniesList, '/companies')
api.add_resource(CompaniesID, '/companies/<int:company_id>')
api.add_resource(CompaniesIDGamesList, '/companies/<int:company_id>/games')

api.add_resource(GamesList, '/games')
api.add_resource(GamesID, '/games/<int:game_id>')
api.add_resource(GamesIDThumbnailsList, '/games/<int:game_id>/thumbnails')
api.add_resource(GamesIDReviewsList, '/games/<int:game_id>/reviews')

api.add_resource(ScreenshotsID, '/screenshots/<int:screenshot_id>')

api.add_resource(UserIDReviewsList, '/users/<int:user_id>/reviews')

api.add_resource(ReviewsID, '/reviews/<int:review_id>')