from mystore.extensions import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user_v2.id'), nullable=False)
    user = db.relationship('User', lazy='joined')

    def __init__(self, **kwargs):
        super(Item, self).__init__(**kwargs)

    def __repr__(self):
        return "<Item %s>" % self.item
