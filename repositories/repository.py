import os
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

class Sqlite(Database):
    def __init__(self, table: str) -> None:
        self.table = table
        self.__create_database()

    def __create_database(self):
        if os.path.exists('database/favorites.db') == False:
            sqlite3.connect('database/favorites.db')    
    
    def open_connection(self):
        self.connection = sqlite3.connect('database/favorites.db')
        self.cursor = self.connection.cursor()
    
    def close_connection(self):
        self.connection.close()

    def create(self, item) -> Any: ...

    def read(self) -> list[Any]:
        self.open_connection()
        response = self.cursor.execute(f'SELECT * FROM {self.table};')
        itens = response.fetchall()
        self.close_connection()
        return itens

    def read_one(self, id) -> Any:
        self.open_connection()
        response = self.cursor.execute(f'SELECT * FROM {self.table} WHERE id = {id};')
        item = response.fetchone()
        self.close_connection()
        return item

    def update(self, item, id) -> Any: ...

    def delete(self, id) -> Any:
        deleted_item = self.read_one(id)
        self.open_connection()
        self.cursor.execute(f'DELETE FROM {self.table} WHERE id = {id};')
        self.connection.commit()
        self.close_connection()
        return deleted_item





class SqliteTopicsRepository(Sqlite):
    def __init__(self) -> None:
        self.driver = super().__init__('topics')
    
    def create(self, item) -> Any:
        self.open_connection()
        id = randint(1,1000) # TODO: Transfer id making to top layer
        item[0] = id
        self.cursor.execute(f'INSERT INTO {self.table} VALUES(?, ?, ?);', item)
        self.connection.commit()
        self.close_connection()
        new_topic = self.read_one(id)
        return new_topic
    
    def update(self, item, id) -> Any:
        self.open_connection()
        self.cursor.execute(
            f"""
                UPDATE topics
                SET name = '{item[0]}',
                link = '{item[1]}'
                WHERE id = {id};
            """
        )
        self.connection.commit()
        self.close_connection()
        new_topic = self.read_one(id)
        return new_topic

class SqliteImagesRepository(Sqlite):
    def __init__(self) -> None:
        self.driver = super().__init__('images')
    
    def create(self, item) -> Any:
        self.open_connection()
        id = randint(1,1000) # TODO: Transfer id making to top layer
        item[0] = id
        self.cursor.execute(f'INSERT INTO {self.table} VALUES(?, ?, ?, ?);', item)
        self.connection.commit()
        self.close_connection()
        new_image = self.read_one(id)
        return new_image
    
    def update(self, item, id) -> Any:
        self.open_connection()
        self.cursor.execute(
            f"""
                UPDATE {self.table} 
                SET title = '{item[0]}', 
                link = '{item[1]}'
                WHERE id = {id};
            """
        )
        self.connection.commit()
        self.close_connection()
        new_image = self.read_one(id)
        return new_image
