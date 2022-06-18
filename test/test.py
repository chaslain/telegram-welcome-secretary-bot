import unittest
from bot.message_parser import MessageParser
from fake_models.fake_telegram import *
import os



class Test(unittest.TestCase):
    def testNoExceptionOnNonJoin(self):
        update: Update = getUpdate()
        MessageParser.getMessages(update)
    
    def testUserHasNullUsername(self):
        update = getUpdate()
        update['message'] = {}
        user = getUser()
        user["first_name"] = "test"
        user["last_name"] = "testington"
        update['message']['new_chat_members'] = [
            user
        ]
        messages = MessageParser.getMessages(update)
        assert(len(messages) == 1)
        print(messages[0].message)
        assert(messages[0].message == "A new person for the welcoming... test testington")
    
    def testMessageSentOnJoin(self):
        update = getUpdate()
        update['message'] = {}
        user = getUser()
        user["first_name"] = "test"
        user["last_name"] = "testington"
        user["username"] = "testy"
        update['message']['new_chat_members'] = [
            user
        ]
        messages = MessageParser.getMessages(update)
        assert(len(messages) == 1)
        assert(messages[0].message == "A new person for the welcoming... test testington (@testy)")
    
    def testMessageNotSentOnNonJoinUpdate(self):
        update = getUpdate()
        update['message'] = {"text": "Hello guys!"}
        messages = MessageParser.getMessages(update)
        assert(len(messages) == 0)
        