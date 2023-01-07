import os
from telegram import Bot, Update
from bot.models.message_to_send import MessageToSend
import random
class MessageParser:

    to_user = os.getenv("SECRETARY_BOT_TO_USER")

    def get_message_string(username):
        random.seed()
        cand = []
        with open("config/responses.txt") as f:
            for line in f:
                cand.append(line)
        
        message_index = random.randrange(0, len(cand) - 1)

        message = cand[message_index]
        return message.replace("[target]", username) \
            .replace("[boss]", MessageParser.to_user)

    def getMessages(update) -> list[MessageToSend]:
        result = []
        print(update)
        if 'message' not in update or \
            update['message'] == None or \
            'new_chat_members' not in update['message'] or \
            update['message']['new_chat_members'] == None:
            return result
        
        chat = update['message']['chat']
        result = []

        for user in update['message']['new_chat_members']:
            name = MessageParser.getFullName(user)
            message = MessageParser.get_message_string(name)
            result.append(MessageToSend(chat['id'], message))
            
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

