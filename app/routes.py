from app import app
from flask import jsonify
from app.models import Currency
from app.schemas import CurrencySchema

@app.route("/", methods=["GET"])
def home():
	return "Hello World"

@app.route("/currencies", methods=["GET"])
def index():
	currencies = Currency.query.all()
	return jsonify(CurrencySchema(many=True).dump(currencies))