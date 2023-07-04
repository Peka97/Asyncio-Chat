import sqlite3
from datetime import datetime
import os
import hashlib

from sqlalchemy import create_engine, select, table
from sqlalchemy.orm import Session
from sqlalchemy.orm import registry
from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, MetaData, ForeignKey

from database.models.server import User, ServerHistory, ServerContacts
from database.models.client import ClientContacts, MessageHistory


class ServerDatabase:
    def __init__(self, db_path="sqlite:///database\\server.sqlite3"):
        self.metadata = MetaData()
        self.engine = create_engine(
            db_path,
            echo=False
        )
        users_table = Table(
            'users',
            self.metadata,
            Column('id', Integer, primary_key=True),
            Column('first_name', String),
            Column('last_name', String),
            Column('username', String),
            Column('password', String),
            Column('salt', String),
            Column('online', Boolean, default=False),
        )
        history_table = Table(
            'history',
            self.metadata,
            Column('id', Integer, primary_key=True),
            Column('logined_at', DateTime, default=datetime.now()),
            Column('ip', String),
            Column('port', String)
        )
        contacts_table = Table(
            'contacts',
            self.metadata,
            Column('id', Integer, primary_key=True),
            Column("user_id", ForeignKey("users.id")),
            Column("friend_id", ForeignKey("users.id")),
        )

        self.metadata.create_all(self.engine)

        self.registry = registry()
        self.registry.map_imperatively(User, users_table)
        self.registry.map_imperatively(ServerContacts, contacts_table)
        self.registry.map_imperatively(ServerHistory, history_table)

    def user_exists(self, username):
        with Session(self.engine) as session:
            query = select(User).filter_by(username=username)
            user = session.scalars(query).first()
            if user is None:
                return False
            return True

    def user_auth(self, username, password):
        with Session(self.engine) as session:
            query = select(User).filter_by(username=username)
            user = session.scalars(query).first()
        if self.check_password(password, user):
            print('ПАРОЛЬ ПРОВЕРЕН')
            return True
        print('ПАРОЛЬ НЕ ПОДХОДИТ')
        return False

    @staticmethod
    def check_password(password, user):
        pswd_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            user.salt,
            100000,
            128
        )
        print(pswd_hash)
        print()
        print(user.password)
        return pswd_hash == user.password

    def user_create(self, first_name, last_name, username, password):
        with Session(self.engine) as session:

            if self.user_exists(username):
                return
            try:
                salt = os.urandom(32)
                pswd_hash = hashlib.pbkdf2_hmac(
                    'sha256',
                    password.encode('utf-8'),
                    salt,
                    100000,
                    128
                )

                user = User(
                    first_name,
                    last_name,
                    username,
                    pswd_hash,
                    salt
                )
                session.add(user)
            except Exception as err:
                print(err)
            else:
                session.commit()

    def user_add_contact(self, user_id, friend_id):
        with Session(self.engine) as session:
            try:
                contact = ServerContacts(user_id, friend_id)
                session.add(contact)
            except Exception:
                pass
            else:
                session.commit()

    def user_get_contacts(self, username: str) -> list | None:
        with Session(self.engine) as session:
            try:
                query = select(User).filter_by(username=username)
                user = session.scalars(query).first()

                query = select(ServerContacts).filter_by(user_id=user.id)
                friends = session.scalars(query).all()
                print(friends)
                friend_ids = [friend.friend_id for friend in friends]
                print(friend_ids)
            except Exception:
                pass
            else:
                return friend_ids

    def contacts_from(self, user_id):
        with Session(self.engine) as session:
            try:
                query = select(ServerContacts).filter_by(user_id=user_id)
                contacts = session.scalars(query).all()
            except Exception:
                pass
            else:
                return contacts

    def history_update(self, ip: str, port: str):
        with Session(self.engine) as session:
            try:
                connected = ServerHistory(ip, port)
                session.add(connected)
            except Exception as err:
                pass
            else:
                session.commit()


class ClientDatabase:
    def __init__(self, username):
        self.metadata = MetaData()
        self.engine = create_engine(
            f"sqlite:///database\\client_{username}.sqlite3",
            echo=False
        )
        contacts_table = Table(
            'contacts',
            self.metadata,
            Column('id', Integer, primary_key=True),
            Column('user_id', Integer),
        )
        message_history_table = Table(
            'message_history',
            self.metadata,
            Column('id', Integer, primary_key=True),
            Column('send_from', Integer),
            Column('text', String),
            Column('dispatch_time', DateTime, default=datetime.now()),
        )

        self.metadata.create_all(self.engine)

        self.registry = registry()
        self.registry.map_imperatively(ClientContacts, contacts_table)
        self.registry.map_imperatively(MessageHistory, message_history_table)

    def message_add(self, from_user_id: int, text: str):
        with Session(self.engine) as session:
            try:
                message = MessageHistory(
                    from_user_id,
                    text,
                )
                session.add(message)
            except Exception:
                pass
            else:
                session.commit()

    def contact_add(self, user_id: int):
        with Session(self.engine) as session:
            try:
                contact = ClientContacts(user_id)
                session.add(contact)
            except Exception:
                pass
            else:
                session.commit()


if __name__ == '__main__':
    # Check Server
    db = ServerDatabase()
    db.user_create('Ivan', 'Karasyov', 'peka97', '12345')
    db.user_create('Kirill', 'Zaharenko', 'fdsatrew', '12345')
    db.user_create('Maxim', 'Frolov', 'FluffyQQ', '12345')
    db.user_add_contact(1, 2)
    db.user_add_contact(1, 3)
    db.history_update('192.168.0.1', 7777)

    # Check Client
    # db = ClientDatabase('peka97')
    # db.message_add(1, 'Hello!')
    # db.message_add(2, 'Hi!')
    # db.contact_add(2)
    # db.contact_add(3)
