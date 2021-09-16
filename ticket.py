from models.repositories import TicketRepo
from schemas.schemas import TicketSchema
from flask import request

from seed import data_upload


ticketRepo = TicketRepo()
ticketSchema = TicketSchema()
ticketListSchema = TicketSchema(many=True)
TICKET_NOT_FOUND = "Ticket not found for id: {}"


def get(id):
  ticket_data = TicketRepo.fetchById(id)
  if ticket_data:
      return ticketSchema.dump(ticket_data)
  return {'message': TICKET_NOT_FOUND.format(id)}, 404

def update(id):
    ticket_data = TicketRepo.fetchById(id)
    ticket_req_json = request.get_json()
    if ticket_data:
      if ticket_req_json.get('ticket_id', None):
        ticket_data.ticket_id = ticket_req_json['ticket_id']
      if ticket_req_json.get('phone', None):
        ticket_data.phone = ticket_req_json['phone']
      if ticket_req_json.get('subject', None):
        ticket_data.subject = ticket_req_json['subject']
      if ticket_req_json.get('intents', None):
        ticket_data.intents = ticket_req_json['intents']
      ticketRepo.update(ticket_data)
      return ticketSchema.dump(ticket_data)
    return {'message': TICKET_NOT_FOUND.format(id)}, 404

def create():
    ticket_req_json = request.get_json()
    ticket_data = ticketSchema.load(ticket_req_json)
    ticketRepo.create(ticket_data)
    return ticketSchema.dump(ticket_data), 201

def getAll():
  data_upload()
  res = ticketRepo.fetchAll()
  return ticketListSchema.dump(res), 200
