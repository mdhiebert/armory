import sqlite3
import unittest

from armory import constants
from armory.backend.armory.armory import Armory
from armory.backend.armory.item import Item
from scripts import create_databases

import random

TEST_DATABASE_FILEPATH = './test/testdb.db'

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

    def test_add_get_remove_item(self):
        arm = Armory(TEST_DATABASE_FILEPATH)
        item_id = 0
        item = Item(item_id, 'Test Item', 'W1234567')

        arm.add_item(item)

        other_item = arm.get_item(item_id)
        
        self.assertEqual(item, other_item)

        arm.remove_item(item)

        with self.assertRaises(KeyError):
            arm.get_item(item_id)

    def test_add_get_many(self):
        arm = Armory(TEST_DATABASE_FILEPATH)
        item_ids = list(set([random.randint(0, 50) for _ in range(random.randint(0, 100))]))
        items = [Item(item_id, 'Fake Item', 'W12456') for item_id in item_ids]

        for item in items:
            arm.add_item(item)
        
        fetched_items = arm.get_all_items()

        self.assertEqual(len(fetched_items), len(item_ids))
        self.assertEqual(set(items), set(fetched_items))

        for item_id in item_ids:
            arm.remove_item(item_id)

        fetched_items = arm.get_all_items()

        self.assertEqual(len(fetched_items), 0)

if __name__ == '__main__':
    unittest.main()