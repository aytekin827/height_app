from height_app import db

class Country(db.Model):
    __tablename__ = 'country'
    
    country_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    continent = db.Column(db.String(64))

    def __repr__(self):
        return f"Country : ({self.country_id}){self.name}"