from datetime import datetime


class Message:
    def __init__(self):
        self.message_id = None
        self.from_user = User()
        self.chat = Chat()
        self.date = datetime.date
        self.text = None

class User:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.username = None
        self.id = None
        self.is_bot = None

class Update:
    def __init__(self):
        self.message = None
        self.update_id = 1
        self.chat_member = None
        self.effective_user = User()

class Chat:
    def __init__(self):
        self.name = None
        self.id = None

class ChatMemberUpdated:
    def __init__(self):
        self.chat = Chat()
        self.from_user = User()
        self.date = datetime.date
        self.old_chat_member = ChatMember()
        self.new_chat_member = ChatMember()

class ChatMember:
    def __init__(self):
        self.user = User()
        self.status = None
        self.is_member = None
        