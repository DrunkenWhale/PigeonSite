from rosemary.extension import db


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    mailbox = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(128))

    # user_message = db.relationship("Message")  #foreign key

    def __init__(self, mailbox, name, password):
        self.id = 0
        self.mailbox = mailbox
        self.name = name
        self.password = password
