from config.log_config import logger as log
import sqlite3 as sqlite


class Sqlite:
    _instance = None
    _db_route = f"db/bank.db"

    def __init__(self, db_route=None):
        if db_route is not None:
            self.connection = sqlite.connect(db_route)
        else:
            self.connection = sqlite.connect(self.__db_route)
        self.cursor = self.connection.cursor()

    @classmethod
    def get_instance(cls, db_route=None):
        if cls._instance is None:
            cls._instance = cls(db_route=db_route)
        return cls._instance

    @classmethod
    def set_db_route(cls, db_route=None):
        if db_route is None:
            return
        cls._db_route = db_route

    @property
    def db_route(self):
        return self._db_route

    @db_route.setter
    def db_route(self, ndb_route):
        self._db_route = ndb_route

    def execute_query(self, query=None):
        if query is None:
            return

        log.info(f"Executing Query Params: {query}")
        return self.cursor.execute(query)

    def execute_many_query(self, *query):
        if query is None:
            return

        log.info(f"Executing Query Params: {query}")
        return self.cursor.executemany(*query)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        if isinstance(exc_val, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()

        self.connection.close()

    def __str__(self):
        return f"""
            connection: {self.connection.__str__()}
            cursor: {self.cursor.__str__()}
        """
