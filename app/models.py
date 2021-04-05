from app import db

class Currency(db.Model):
    __tablename__ = "currencies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    code = db.Column(db.String(8))
    value = db.Column(db.Float)
    date = db.Column(db.Date)
    flag = None

    @property
    def flag(self):
        return "/images/flags-png/" + self.code.lower() + ".png"

    def __init__(self, name, code, value, date):
        self.name = name
        self.code = code
        self.value = value
        self.date = date