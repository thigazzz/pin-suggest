import sqlite3
from typing import Any
from random import randint
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def create(self, item)-> Any:  ...

    @abstractmethod
    def read(self) -> list[Any]: ...

    @abstractmethod
    def read_one(self, id) -> Any: ...

    @abstractmethod
    def update(self, item, id) -> Any: ...

    @abstractmethod
    def delete(self, id) -> None: ...
import os

class SqliteDatabase(Database):
    def __init__(self) -> None:
        self.__setup()
    
    def __setup(self):
        self.__create_database()
        self.__open_connection()

    def __create_database(self):
        if os.path.exists('database/favorites.db') == False:
            sqlite3.connect('database/favorites.db')    
    
    def __open_connection(self):
        self.connection = sqlite3.connect('database/favorites.db')
        self.cursor = self.connection.cursor()
    
    def __close_connection(self):
        self.connection.close()

    def create(self, item) -> Any:
        self.__open_connection()
        id = randint(1,1000) # TODO: Transfer id making to top layer
        item[0] = id
        self.cursor.execute('INSERT INTO favorites VALUES(?, ?, ?, ?);', item)
        self.connection.commit()
        self.__close_connection()
        new_item = self.read_one(id)
        return new_item

    def read(self) -> list[Any]:
        self.__open_connection()
        response = self.cursor.execute('SELECT * FROM favorites;')
        itens = response.fetchall()
        self.__close_connection()
        return itens

    def read_one(self, id) -> Any:
        self.__open_connection()
        response = self.cursor.execute(f'SELECT * FROM favorites WHERE id = {id};')
        item = response.fetchone()
        self.__close_connection()
        return item

    def update(self, item, id) -> Any:
        self.__open_connection()
        self.cursor.execute(
            f"""
                UPDATE favorites 
                SET title = '{item[0]}', 
                link = '{item[1]}', 
                topic = '{item[2]}'
                WHERE id = {id};
            """
        )
        self.connection.commit()
        self.__close_connection()
        new_item = self.read_one(id)
        return new_item

    def delete(self, id) -> Any:
        deleted_item = self.read_one(id)
        self.__open_connection()
        self.cursor.execute(f'DELETE FROM favorites WHERE id = {id};')
        self.connection.commit()
        self.__close_connection()
        return deleted_item
