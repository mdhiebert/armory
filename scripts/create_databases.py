import sqlite3
from armory.util.sql import *
from armory.constants import CREATE_ITEMS_TABLE_COMMAND, CREATE_PERMANENT_ACCOUNTABILITY_TABLE_COMMAND, CREATE_TEMPORARY_ACCOUNTABILITY_TABLE_COMMAND, CREATE_USER_TABLE_COMMAND, MASTER_DB_NAME, MASTER_DB_FILEPATH

def create_databases():
    create_database(MASTER_DB_NAME)

    with sqlite3.connect(MASTER_DB_FILEPATH) as c:
        c.execute(CREATE_ITEMS_TABLE_COMMAND)
        c.execute(CREATE_PERMANENT_ACCOUNTABILITY_TABLE_COMMAND)
        c.execute(CREATE_TEMPORARY_ACCOUNTABILITY_TABLE_COMMAND)
        c.execute(CREATE_USER_TABLE_COMMAND)

if __name__ == '__main__':
    create_databases()