
# DATABASES

MASTER_DB_NAME = 'master_database'
MASTER_DB_FILEPATH = f'./data/{MASTER_DB_NAME}.db'

ITEMS_TABLE_NAME = 'items'
CREATE_ITEMS_TABLE_COMMAND = f'''
          CREATE TABLE IF NOT EXISTS {ITEMS_TABLE_NAME}
          ([item_id] INTEGER PRIMARY KEY, [item_name] TEXT, [serial_number] TEXT)
          '''

PERMANENT_ACCOUNTABILITY_TABLE_NAME = 'permanent_accountability'
CREATE_PERMANENT_ACCOUNTABILITY_TABLE_COMMAND = f'''
          CREATE TABLE IF NOT EXISTS {PERMANENT_ACCOUNTABILITY_TABLE_NAME}
          ([item_id] INTEGER PRIMARY KEY, [user_id] INTEGER)
          '''

TEMPORARY_ACCOUNTABILITY_TABLE_NAME = 'temporary_accountability'
CREATE_TEMPORARY_ACCOUNTABILITY_TABLE_COMMAND = f'''
          CREATE TABLE IF NOT EXISTS {TEMPORARY_ACCOUNTABILITY_TABLE_NAME}
          ([item_id] INTEGER PRIMARY KEY, [datetime] DATETIME, [in-or-out] TEXT, [user_id] INTEGER)
          '''

USER_TABLE_NAME = 'user'
CREATE_USER_TABLE_COMMAND = f'''
          CREATE TABLE IF NOT EXISTS
          {USER_TABLE_NAME}
          ([user_id] INTEGER PRIMARY KEY, [company] TEXT, [platoon] INTEGER, [last_name] TEXT, [first_name] TEXT)
          '''