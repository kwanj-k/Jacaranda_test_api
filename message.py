from models.repositories import MessageRepo
from schemas.schemas import MessageSchema
from flask import request

msgRepo = MessageRepo()
msgSchema = MessageSchema()
msgListSchema = MessageSchema(many=True)
MSG_NOT_FOUND = "Message not found for id: {}"


def get(id):
  msg_data = msgRepo.fetchById(id)
  if msg_data:
      return msgSchema.dump(msg_data)
  return {'message': MSG_NOT_FOUND.format(id)}, 404


def update(id):
    msg_data = msgRepo.fetchById(id)
    msg_req_json = request.get_json()
    if msg_data:
      if msg_req_json.get('id', None):
        msg_data.id = msg_req_json['id']
      if msg_req_json.get('user_id', None):
        msg_data.user_id = msg_req_json['user_id']
      if msg_req_json.get('created_at', None):
        msg_data.created_at = msg_req_json['created_at']
      if msg_req_json.get('updated_at', None):
        msg_data.updated_at = msg_req_json['updated_at']
      if msg_req_json.get('description', None):
        msg_data.description = msg_req_json['description']
      if msg_req_json.get('incoming', None):
        msg_data.incoming = msg_req_json['incoming']
      msgRepo.update(msg_data)
      return msgSchema.dump(msg_data)
    return {'message': MSG_NOT_FOUND.format(id)}, 404


def create():
    msg_req_json = request.get_json()
    msg_data = msgSchema.load(msg_req_json)
    msgRepo.create(msg_data)
    return msgSchema.dump(msg_data), 201


def getAll():
    return msgListSchema.dump(msgRepo.fetchAll()), 200
