from server.extensions import db

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship("Appearance", back_populates="episode", cascade="all, delete")

    def to_dict(self, include_relationships=False):
        data = {
            "id": self.id,
            "date": self.date,
            "number": self.number,
        }

        if include_relationships:
            data["appearances"] = [a.to_dict() for a in self.appearances]

        return data
