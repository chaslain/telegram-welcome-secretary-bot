from telegram import Message, Update

from models.message_to_send import MessageToSend

class MessageParser:
    def handleMessage(update: Update):
        
        if update.chat_member == None:
            return
        
    def getMessages(update: Update) -> list[MessageToSend]:
        
