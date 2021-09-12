
from db import db
from models.entities import Ticket, Message
from typing import List


class TicketRepo:

  def create(self, ticket):
    db.session.add(ticket)
    db.session.commit()

  def fetchById(_id):
    return db.session.query(Ticket).filter_by(id=_id).first()


  def fetchAll(self):
    from sqlalchemy.orm import joinedload
    return Ticket.query.options(joinedload('messages'))
  
  def fetchTktMsgAll(self):
    return db.session.query(Ticket).all()

        
    def update(self, ticket_data):
        db.session.merge(ticket_data)
        db.session.commit()


class MessageRepo:
  
    def create(self, message):
        db.session.add(message)
        db.session.commit()

    def fetchById(_id) -> 'Message':
        return db.session.query(Message).filter_by(id=_id).first()

    def fetchAll(self) -> List['Message']:
        return db.session.query(Message).all()

    def update(self, message_data):
        db.session.merge(message_data)
        db.session.commit()
