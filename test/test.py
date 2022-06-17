import unittest
from telegram import ChatMember, ChatMemberUpdated, Update
from telegram import Message
from message_parser import MessageParser




class Test(unittest.TestCase):

    def noExceptionOnNonJoin():
        update: Update = Update()

        update.message = Message()
        MessageParser.handleMessage(update)
    
    def messageSentOnJoin():
        update: Update = Update()
        update.chat_member.new_chat_member.is_member = True
        update.chat_member.old_chat_member.is_member = False
        update.chat_member.from_user.name = "test"
        update.chat_member.from_user.full_name = "test testingson"
        update.chat_member.chat.id = "1234"
        update.chat_member.from_user.username = "123123"
        messages = MessageParser.getMessages(update)
        assert(messages[0].to_chat_id == "1234")
        assert(messages[0].message == "A new person for the welcoming... test testingson (testy)")
    
    def messageNotSentOnNonJoinUpdate():
        update: Update = Update();
        update.chat_member.new_chat_member.is_member = True
        update.chat_member.old_chat_member.is_member = True
        update.chat_member.from_user.full_name = "test testingson"
        update.chat_member.chat.id = "1234"
        update.chat_member.from_user.username = "testy"
        messages = MessageParser.getMessages(update)
        assert(len(messages) == 0)

    def messageNotSentOnNonUpdate():
        update: Update = Update();
        update.message.text = "What is going on guys??"
        messages = MessageParser.getMessages(update)
        update.chat_member.from_user.full_name = "test testingson"
        update.chat_member.chat.id = "1234"
        update.chat_member.from_user.username = "testy"
        assert(len(messages) == 0)
        