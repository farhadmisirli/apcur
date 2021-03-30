from app import db

class Currency(db.Model):
    __tablename__ = "currencies"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(8))
    value = db.Column(db.Float)
    date = db.Column(db.Date)

    def __init__(self, code, value, date):
        self.code = code
        self.value = value
        self.date = date
