import os
from telegram import Update
from bot.models.message_to_send import MessageToSend

class MessageParser:

    to_user = os.getenv("SECRETARY_BOT_TO_USER")

    def getMessages(update: Update) -> list[MessageToSend]:
        result = []
        if update.chat_member == None:
            return result
        
        if update.chat_member.old_chat_member.is_member == False\
            and update.chat_member.new_chat_member.is_member == True:

            msg = None

            if update.effective_user.username != None:
                msg = "A new person for the welcoming... " + update.effective_user.full_name \
                + " (" + update.effective_user.username + ")"
            else:
                msg = "A new person for the welcoming... " + update.effective_user.full_name

            message = MessageToSend(MessageParser.to_user, msg)
            return [message]
        return []
