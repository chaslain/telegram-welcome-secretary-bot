from telegram import Update
from bot.models.message_to_send import MessageToSend

from bot.models.message_to_send import MessageToSend

class MessageParser:
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

            message = MessageToSend("@Jonkler", msg)
            return [message]
        return []
