from flask_smorest import Blueprint
from marshmallow import ValidationError
from app.models import db, User, Category, Currency, Record
from app.schemas import UserSchema, CategorySchema, CurrencySchema, RecordSchema

bp = Blueprint('api', __name__, url_prefix='/api')

# User Endpoints
@bp.route('/users', methods=['POST'])
@bp.arguments(UserSchema)
@bp.response(201, UserSchema)
def create_user(data):
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return user

@bp.route('/users', methods=['GET'])
@bp.response(200, UserSchema(many=True))
def get_users():
    return User.query.all()

# Category Endpoints
@bp.route('/categories', methods=['POST'])
@bp.arguments(CategorySchema)
@bp.response(201, CategorySchema)
def create_category(data):
    category = Category(**data)
    db.session.add(category)
    db.session.commit()
    return category

@bp.route('/categories', methods=['GET'])
@bp.response(200, CategorySchema(many=True))
def get_categories():
    return Category.query.all()

# Currency Endpoints
@bp.route('/currencies', methods=['POST'])
@bp.arguments(CurrencySchema)
@bp.response(201, CurrencySchema)
def create_currency(data):
    currency = Currency(**data)
    db.session.add(currency)
    db.session.commit()
    return currency

@bp.route('/currencies', methods=['GET'])
@bp.response(200, CurrencySchema(many=True))
def get_categories():
    return Category.query.all()

# Record Endpoints
@bp.route('/records', methods=['POST'])
@bp.arguments(RecordSchema)
@bp.response(201, RecordSchema)
def create_record(data):
    record = Record(**data)
    db.session.add(record)
    db.session.commit()
    return record

@bp.route('/records/user/<int:user_id>', methods=['GET'])
@bp.response(200, RecordSchema(many=True))
def get_user_records(user_id):
    category_records = Record.query.filter_by(user_id=user_id).all()
    return category_records

@bp.route('/records/category/<int:category_id>/user/<int:user_id>', methods=['GET'])
@bp.response(200, RecordSchema(many=True))
def get_category_records(user_id, category_id):
    category_records = Record.query.filter_by(category_id=category_id, user_id=user_id).all()
    return category_records

@bp.errorhandler(ValidationError)
def handle_validation_error(e):
    return {"message": str(e)}, 400

@bp.errorhandler(Exception)
def handle_exception(e):
    print(e)
    return {"message": "An internal error occured.", "error": str(e)}, 500
