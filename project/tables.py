from app import database
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class tickets(database.Model):
    ticket_id = database.Column(database.Integer, primary_key=True)
    create_datetime = database.Column(database.DateTime, default=datetime.now())
    change_datetime = database.Column(database.DateTime, default=datetime.now())
    title = database.Column(database.Text)
    body = database.Column(database.Text)
    email = database.Column(database.String(50))
    status = database.Column(database.String(20))
    comments_list = relationship("comments", lazy='select')


class comments(database.Model):
    comment_id = database.Column(database.Integer, primary_key=True)
    ticket_id = database.Column(database.Integer, ForeignKey("tickets.ticket_id"))
    create_datetime = database.Column(database.DateTime, default=datetime.now())
    email = database.Column(database.String(50))
    comment = database.Column(database.Text)
