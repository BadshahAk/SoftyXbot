import threading

from sqlalchemy import Column, String

from SoftyXbot.modules.sql import BASE, SESSION


class SoftyChats(BASE):
    __tablename__ = "Softy_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


SoftyChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_Softy(chat_id):
    try:
        chat = SESSION.query(SoftyChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_Softy(chat_id):
    with INSERTION_LOCK:
        Softychat = SESSION.query(SoftyChats).get(str(chat_id))
        if not Softychat:
            Softychat = SoftyChats(str(chat_id))
        SESSION.add(Softychat)
        SESSION.commit()


def rem_Softy(chat_id):
    with INSERTION_LOCK:
        Softychat = SESSION.query(SoftyChats).get(str(chat_id))
        if Softychat:
            SESSION.delete(Softychat)
        SESSION.commit()
