import json
import bot.message_parser
import bot.message_sender
from telegram.update import Update

def handler(event, context):

    dict = json.loads(event)
    update = Update(**dict)
    sender = bot.message_sender.MessageSender()
    sender.sendMessages(bot.message_parser.MessageParser.getMessages(update))

    return {
        'statusCode': 200
    }