import jsonpickle
import telegram
import message_parser
import message_sender

def handler(event, context):

    update = jsonpickle.decode(event, classes=[telegram.Update]) 
    sender = message_sender.MessageSender()
    sender.sendMessages(message_parser.MessageParser.getMessages(update))

    return {
        'statusCode': 200
    }