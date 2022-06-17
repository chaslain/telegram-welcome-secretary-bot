from fake_models.models import User, Message, Update, ChatMember, ChatMemberUpdated, Chat

def getUser() -> User:
    user = User()
    return user


def getMessage() -> Message:
    return Message()

def getChat() -> Chat:
    return Chat()

def getUpdate() -> Update:
    return Update()

def getChatMember() -> ChatMember:
    return ChatMember()

def getChatMemberUpdated() -> ChatMemberUpdated:
    return ChatMemberUpdated()