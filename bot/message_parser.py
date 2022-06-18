import os
from telegram import Update
from bot.models.message_to_send import MessageToSend

class MessageParser:

    to_user = os.getenv("SECRETARY_BOT_TO_USER")

    def getMessages(update) -> list[MessageToSend]:
        result = []
        print(update)
        if 'message' not in update or \
            update['message'] == None or \
            'new_chat_members' not in update['message'] or \
            update['message']['new_chat_members'] == None:
            return result
        
        result = []
        for user in update['message']['new_chat_members']:
            msg = None

            if 'username' in user and user['username'] != None:
                msg = "A new person for the welcoming... " + MessageParser.getFullName(user) \
                + " (@" + user['username'] + ")"
            else:
                msg = "A new person for the welcoming... " + MessageParser.getFullName(user)

            result.append(MessageToSend(MessageParser.to_user, msg))
            
        return result
    
    def getFullName(user):
        result = ""
        if "first_name" in user:
            result += user["first_name"]
        elif "last_name" in user:
            return user["last_name"]
        
        if "last_name" in user:
            result += " " + user["last_name"]
        
        return result

