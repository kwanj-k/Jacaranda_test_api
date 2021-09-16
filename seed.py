import pandas as pd
import json
import re

import json
from db import db
from models.entities import Ticket, Message
from models.repositories import MessageRepo, TicketRepo
from schemas.schemas import TicketSchema, MessageSchema

ticketSchema = TicketSchema()
msgSchema = MessageSchema()

ticketRepo = MessageRepo()
msgRepo = TicketRepo()


def data_upload():
  tickets = []
  messages = []
  subjects_df = pd.read_excel('msgs.xlsx', sheet_name='Subjects')
  messages_df = pd.read_excel('msgs.xlsx', sheet_name='Messages')
  merged = pd.merge(subjects_df, messages_df, on='ticket_id')
  merged_list = merged.values.tolist()
  
  for item in merged_list:
    ticket_id = item[0]
    msg_id = item[3]
    incoming = item[4]
    user_id = item[5]
    created_at = item[6]
    phone = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', item[1])
    sub_index = item[1].find("]") + 1
    subject = item[1][sub_index:]
    
    if item[2].find("Detected intent:") > -1:
      intent_index = item[2].find(":") + 1
      intent_index_end = item[2].find("(") - 1
      intent = item[intent_index : intent_index_end]
      des_index = item[2].find(")") + 1
      description = item[des_index : ]
    else:
      description = item[2]
      intent = None
    tkt = {
      "ticket_id": ticket_id,
      "phone": phone[0] if len(phone) > 0 else '',
      "subject": subject,
      "intents": [intent] if intent else []
    }
    msg = {
      "id": msg_id,
      "user_id": user_id,
      "ticket_id": ticket_id,
      "created_at": 'test',
      "description": description,
      "incoming": incoming
    }
    import pdb; pdb.set_trace()
    tkt_json = json.dumps(tkt)
    ticket_data = ticketSchema.load(tkt_json)
    #msg_data = ticketSchema.load(msg)
    ticketRepo.create(tkt)
    #msgRepo.create(msg)
  return
