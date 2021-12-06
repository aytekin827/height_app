from height_app import db

class Parent(db.Model):
    __tablename__ = 'parent'
    
    id = db.Column(db.Integer(), primary_key=True)
    father_name = db.Column(db.String(64), nullable=False)
    mother_name = db.Column(db.Integer(),nullable=False)
    father_height = db.Column(db.Integer(),nullable=False)
    mother_height = db.Column(db.Integer(),nullable=False)
    father_weight = db.Column(db.Integer(),nullable=False)
    mother_weight = db.Column(db.Integer(),nullable=False)

    def __repr__(self):
        return f"Parents : ({self.id}){self.father_name} and {self.mother_name}"