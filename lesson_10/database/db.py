import sqlite3
from datetime import datetime

from sqlalchemy import create_engine, select, table
from sqlalchemy.orm import Session
from sqlalchemy.orm import registry
from sqlalchemy import Table, Column, Integer, String, Boolean, DateTime, MetaData, ForeignKey

from database.models.users import User, Contacts
from database.models.history import History


class ServerDatabase:
    def __init__(self, db_path):
        self.metadata = MetaData()
        self.engine = create_engine(
            db_path,
            echo=True
        )
        users_table = Table(
            'users',
            self.metadata,
            Column('id', Integer, primary_key=True),
            Column('first_name', String),
            Column('last_name', String),
            Column('password', String),
            Column('online', Boolean),
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
        self.registry.map_imperatively(Contacts, contacts_table)
        self.registry.map_imperatively(History, history_table)

    def user_find(self, first_name, last_name):
        with Session(self.engine) as session:
            query = select(User).filter_by(
                first_name=first_name, last_name=last_name
            )
            user = session.scalars(query).all()
            if len(user) > 0:
                return True
        return False

    def user_create(self, first_name, last_name, password):
        with Session(self.engine) as session:
            user_is_exists = self.user_find(first_name, last_name)

            if user_is_exists:
                return

            try:
                user_1 = User(
                    first_name,
                    last_name,
                    password
                )
                session.add(user_1)
            except Exception:
                pass
            else:
                session.commit()

    def user_add_contact(self, user_id, friend_id):
        with Session(self.engine) as session:
            try:
                contact = Contacts(user_id, friend_id)
                session.add(contact)
            except Exception:
                pass
            else:
                session.commit()

    def contacts_from(self, user_id):
        with Session(self.engine) as session:
            try:
                query = select(Contacts).filter_by(user_id=user_id)
                contacts = session.scalars(query).all()
            except Exception:
                pass
            else:
                return contacts

    def history_update(self, ip: str, port: str):
        with Session(self.engine) as session:
            try:
                connected = History(ip, port)
                session.add(connected)
            except Exception as err:
                pass
            else:
                session.commit()


class ClientDatabase:
    def __init__(self, username):
        self.metadata = MetaData()
        self.engine = create_engine(
            f"sqlite:////home/peka97/Asyncio-Chat/lesson_10/database/client_{username}.sqlite3",
            echo=True
        )
        users_table = Table(
            'users',
            self.metadata,
            Column('id', Integer, primary_key=True),
            Column('first_name', String),
            Column('last_name', String),
            Column('password', String),
            Column('online', Boolean),
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
        self.registry.map_imperatively(Contacts, contacts_table)
        self.registry.map_imperatively(History, history_table)


if __name__ == '__main__':
    pass
    # db = ServerDatabase()
    # db.user_create('Ivan', 'Karasyov', '12345qwert')
    # db.user_create('Kirill', 'Zaharenko', 'fdsatrew')
    # db.user_create('Maxim', 'Frolov', '09876543')
    # db.user_add_contact(1, 2)
    # db.user_add_contact(1, 3)
    # db.history_update('192.168.0.1')
