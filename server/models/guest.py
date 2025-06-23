from server.app import db

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)

    # A guest can appear in many episodes
    appearances = db.relationship("Appearance", backref="guest", cascade="all, delete")
