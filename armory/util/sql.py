import sqlite3

def create_database(database_name):
    try:
        sqlite3.connect(f'./data/{database_name}.db')
    except:
        pass