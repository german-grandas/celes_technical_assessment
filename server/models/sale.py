from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class SaleDataModel(db.Model):
    __tablename__ = "sales"
    id = db.Column(db.Integer, primary_key=True)
    KeyEmployee = db.Column(db.String(255), nullable=False)
    KeyProduct = db.Column(db.String(255), nullable=False)
    KeyStore = db.Column(db.String(255), nullable=False)
    KeyDate = db.Column(db.Date, nullable=False)
    TicketId = db.Column(db.String(255), nullable=False)
    Amount = db.Column(db.Float, nullable=False)
    CostAmount = db.Column(db.Float, nullable=False)
    DiscAmount = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "KeyProduct": self.KeyProduct,
            "KeyStore": self.KeyStore,
            "KeyDate": self.KeyDate.strftime("%Y-%m-%d"),
            "Amount": self.Amount,
            "CostAmount": self.CostAmount,
            "DiscAmount": self.DiscAmount,
        }
