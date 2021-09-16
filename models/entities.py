from db import db
from sqlalchemy.dialects import postgresql


class Message(db.Model):
  __tablename__ = "messages"

  pk = db.Column(db.Integer, primary_key=True)
  id = db.Column(db.Integer, nullable=False)
  # ticket_id = db.Column(db.Integer, db.ForeignKey(
  #     "tickets.ticket_id"), nullable=False)
  user_id = db.Column(db.Integer, nullable=False)
  ticket_id = db.Column(db.Integer, nullable=False)
  created_at = db.Column(db.String(100), nullable=False)
  updated_at = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(200), nullable=False)
  incoming = db.Column(db.Boolean, nullable=False)
  # ticket = db.relationship('Ticket',
  #                            backref=db.backref('messages', lazy=True))

  def __repr__(self):
    return 'Message(id=%d,user_id=%s,)' % (self.id, self.user_id)

  def json(self):
    return {
        'id': self.id,
        'user_id': self.user_id,
        'created_at': self.created_at,
        'updated_at': self.updated_at,
        'description': self.description
    }


class Ticket(db.Model):
    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    intents = db.Column(postgresql.ARRAY(db.String))
