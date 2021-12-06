from height_app import db

class Users(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer(), primary_key=True)
    # username = db.Column(db.String(64), nullable=False)
    height = db.Column(db.Integer(),nullable=False)
    weight = db.Column(db.Integer(),nullable=False)
    father_height = db.Column(db.Integer(),nullable=False)
    mother_height = db.Column(db.Integer(),nullable=False)
    # sex = db.Column(db.Boolean(),nullable=False)
    # birth = db.Column(db.DateTime(),nullable=False)
    # parent_id = db.Column(db.Integer,nullable=False)
    # country_code = db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"User : ({self.id}){self.height},{self.weight}"

def add_user(raw_user):
    new_user = Users(
        id = raw_user['id'],
        # username = raw_user['username'],
        height = raw_user['height'],
        weight = raw_user['weight'],
        father_height = raw_user['father_height'],
        mother_height = raw_user['mother_height'],
        # sex = raw_user['sex'],
        # birth = raw_user['birthday'],
        # parent_id = raw_user['parent_id'],
        # country_code = raw_user['country_code']
    )

    if Users.query.filter(Users.id == new_user.id).first() == None:
        db.session.add(new_user)
        db.session.commit()

def get_users():
    return Users.query.order_by("id").all()

def delete_user(user_id):
    user = Users.query.filter(Users.id == user_id).first()
    db.session.delete(user)
    db.session.commit()

def update_user(user_id,height=None,weight=None,father_height=None,mother_height=None):
    user = Users.query.filter(Users.id == user_id).first()
    if height:
        user.height = height
    if weight:
        user.weight = weight
    if father_height:
        user.father_height = father_height
    if mother_height:
        user.mother_height = mother_height
    db.session.commit()
