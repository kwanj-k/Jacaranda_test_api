from main import ma
from db import db
from marshmallow import Schema, fields

from models.entities import Ticket, Message


class MessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message
        load_instance = True


class TicketSchema(ma.SQLAlchemyAutoSchema):
  incoming_messages = fields.Method('get_incoming_messages')
  outgoing_messages = fields.Method('get_outgoing_messages')

  def get_incoming_messages(self, obj):
    msgListSchema = MessageSchema(many=True)
    msgs = db.session.query(Message).filter(
        Message.ticket_id==obj.ticket_id, Message.incoming==True)
    return msgListSchema.dump(msgs)
  
  def get_outgoing_messages(self, obj):
    msgListSchema = MessageSchema(many=True)
    msgs = db.session.query(Message).filter(
        Message.ticket_id == obj.ticket_id, Message.incoming == False)
    return msgListSchema.dump(msgs)
  
  class Meta:
    model = Ticket
    load_instance = True
