from app import database
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Tickets(database.Model):
    __tablename__ = 'tickets'
    ticket_id = database.Column(database.Integer, primary_key=True)
    create_datetime = database.Column(database.DateTime, default=datetime.now())
    change_datetime = database.Column(database.DateTime, default=datetime.now())
    title = database.Column(database.Text)
    body = database.Column(database.Text)
    email = database.Column(database.String(50))
    status = database.Column(database.String(20), default='opened')
    comments_list = relationship("comments", lazy='select')

    def as_dict(self) -> dict:
        return {
            "ticket_id": self.ticket_id,
            "create_datetime": self.create_datetime,
            "change_datetime": self.change_datetime,
            "title": self.title,
            "body": self.body,
            "email": self.email,
            "status": self.status,
            "comments": [comment.as_dict() for comment in self.comments_list],
        }


class Comments(database.Model):
    __tablename__ = 'comments'
    comment_id = database.Column(database.Integer, primary_key=True)
    ticket_id = database.Column(database.Integer, ForeignKey("tickets.ticket_id"))
    create_datetime = database.Column(database.DateTime, default=datetime.now())
    email = database.Column(database.String(50))
    comment = database.Column(database.Text)

    def as_dict(self) -> dict:
        return {
            "comment_id": self.comment_id,
            # "ticket_id": self.ticket_id,
            "create_datetime": self.create_datetime,
            "email": self.email,
            "comment": self.comment,
        }
