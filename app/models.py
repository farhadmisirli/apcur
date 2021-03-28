from app import db

class Currency(db.Model):
    __tablename__ = "currencies"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(8))
    flag = db.Column(db.String(32))
    status = db.Column(db.BOOLEAN)

    def __init__(self, code, flag, status):
        self.code = code
        self.flag = flag
        self.status = status
