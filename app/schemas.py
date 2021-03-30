from app import ma
from app.models import Currency

class CurrencySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Currency