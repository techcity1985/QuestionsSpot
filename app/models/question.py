from .user import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Question %r>' % self.question_text
