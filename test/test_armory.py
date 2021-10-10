import sqlite3
import unittest

from armory import constants
from scripts import create_databases

class TestArmory(unittest.TestCase):


    # TABLE INITIALIZATION

    def _does_table_exist(self, table_name):
        with sqlite3.connect(constants.MASTER_DB_FILEPATH) as conn:
            c = conn.cursor()
            c.execute(f''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table_name}' ''')
            return c.fetchone()[0]==1
    
    def test_database_initializaton(self):
        create_databases.create_databases()

        self.assertTrue(self._does_table_exist(constants.ITEMS_TABLE_NAME), f'{constants.ITEMS_TABLE_NAME} does not exist.')
        self.assertTrue(self._does_table_exist(constants.PERMANENT_ACCOUNTABILITY_TABLE_NAME), f'{constants.PERMANENT_ACCOUNTABILITY_TABLE_NAME} does not exist.')
        self.assertTrue(self._does_table_exist(constants.TEMPORARY_ACCOUNTABILITY_TABLE_NAME), f'{constants.TEMPORARY_ACCOUNTABILITY_TABLE_NAME} does not exist.')

if __name__ == '__main__':
    unittest.main()