from app import db
from app.config import common_conf as cnf

class Currency(db.Model):
    __tablename__ = "currencies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    code = db.Column(db.String(8))
    value = db.Column(db.Float)
    date = db.Column(db.Date)

    @property
    def flag_png(self):
        return cnf["base_url"]+"/images/flags-png/" + self.code.lower() + ".png"

    @property
    def flag_svg(self):
        return cnf["base_url"] + "/images/flags-svg/" + self.code.lower() + ".svg"

    def __init__(self, name, code, value, date):
        self.name = name
        self.code = code
        self.value = value
        self.date = date