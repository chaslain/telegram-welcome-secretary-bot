import unittest
from bot.message_parser import MessageParser
from fake_models.fake_telegram import *



class Test(unittest.TestCase):

    def testNoExceptionOnNonJoin(self):
        update: Update = getUpdate()
        MessageParser.getMessages(update)
    
    def testUserHasNullUsername(self):
        update: Update = getUpdate()
        update.chat_member = getChatMemberUpdated()
        update.chat_member.new_chat_member = getChatMember()
        update.chat_member.new_chat_member.is_member = True
        update.chat_member.old_chat_member.is_member = False
        update.effective_user.full_name = "test testingson"
        update.chat_member.chat.id = "1234"
        update.effective_user.id = "111"
        update.effective_user.username = None
        messages = MessageParser.getMessages(update)
        assert(messages[0].to_chat_id == "@Jonkler")
        assert(messages[0].message == "A new person for the welcoming... test testingson")
    
    def testMessageSentOnJoin(self):
        update: Update = getUpdate()
        update.chat_member = getChatMemberUpdated()
        update.chat_member.new_chat_member = getChatMember()
        update.chat_member.new_chat_member.is_member = True
        update.chat_member.old_chat_member.is_member = False
        update.effective_user.full_name = "test testingson"
        update.chat_member.chat.id = "1234"
        update.effective_user.username = "testy"
        messages = MessageParser.getMessages(update)
        assert(messages[0].to_chat_id == "@Jonkler")
        assert(messages[0].message == "A new person for the welcoming... test testingson (testy)")
    
    def testMessageNotSentOnNonJoinUpdate(self):
        update: Update = getUpdate();
        update.chat_member = ChatMemberUpdated()
        update.chat_member.new_chat_member.is_member = True
        update.chat_member.old_chat_member.is_member = True
        update.effective_user.full_name = "test testingson"
        update.chat_member.chat.id = "1234"
        update.effective_user.id = "testy"
        messages = MessageParser.getMessages(update)
        assert(len(messages) == 0)

    def testMessageNotSentOnNonUpdate(self):
        update: Update = getUpdate();
        update.message = Message()
        update.message.text = "What is going on guys??"
        messages = MessageParser.getMessages(update)
        update.effective_user.full_name = "test testingson"
        update.message.chat.id = "1234"
        update.effective_user.id = "testy"
        assert(len(messages) == 0)
        