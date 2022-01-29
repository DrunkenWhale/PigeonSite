from rosemary.extension import db


class User(db.Model):
    mailbox = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(128))

    # user_message = db.relationship("Message")  #foreign key

    def __init__(self, mailbox, name, password):
        self.mailbox = mailbox
        self.name = name
        self.password = password
