from app import app
from app.models import Currency
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)


class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Currency

@app.route("/", methods=["GET"])
def home():
	return "Hello World"


@app.route("/currencies", methods=["GET"])
def index():

	currencies = Currency.query.all()

	return NoteSchema(many=True).dump(currencies)




