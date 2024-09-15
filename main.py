from config.log_config import logger as log
from config import sqlite_config as sqlte

import os
import glob


def setup():
    db_file = glob.glob(os.path.join("db", "*.db"))
    existing_db_route = None

    if db_file:
        existing_db_route = db_file[0]
        log.info(f"Existing Database File: {existing_db_route}")

        if len(db_file) > 1:
            log.warning("Multiple Database Files Found, Removing Extra Files...")
            for file in db_file[1:]:
                os.remove(file)

    sqlite_instance = sqlte.Sqlite.get_instance(existing_db_route)

    # sqlite_instance.execute_query("""
    #     INSERT INTO user (name, email, password, is_active, is_superuser)
    #     VALUES ('admin', 'admin.lock@gmail.com', 'admin123', 1, 1)
    # """)

    for row in sqlite_instance.execute_query("""SELECT * FROM user"""):
        log.info(row)


if __name__ == "__main__":
    setup()
