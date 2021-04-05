from app import app
from flask import jsonify
from app.models import Currency
from app.schemas import CurrencySchema
from datetime import date
from app import db

today = date.today()

@app.route("/", methods=["GET"])
def home():
	return "Hello World"

@app.route("/currencies", methods=["GET"])
def index():
	currencies = Currency.query.filter_by(date=today.strftime("%Y-%m-%d")).order_by(Currency.id).all()
	return jsonify(CurrencySchema(many=True).dump(currencies))