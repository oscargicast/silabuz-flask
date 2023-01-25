class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)