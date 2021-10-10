import sqlite3

from armory.backend.armory.abstract import AbstractArmory
from armory.backend.armory.item import Item
from armory.backend.armory.soldier import Soldier
from armory.constants import ITEMS_TABLE_NAME, PERMANENT_ACCOUNTABILITY_TABLE_NAME, TEMPORARY_ACCOUNTABILITY_TABLE_NAME

from typing import List

class Armory(AbstractArmory):
    def __init__(self, database_filepath) -> None:
        self.database_filepath = database_filepath

    def get_item(self, item_id: int) -> Item:
        with sqlite3.connect(self.database_filepath) as conn:
            c = conn.cursor()
            c.execute('''SELECT item_id,item_name,serial_number FROM ? WHERE item_id = ?''', ITEMS_TABLE_NAME, item_id)

            results = c.fetchall()

            # sanitization

            assert len(results) < 2, f'Found {len(results)} items with item_id {item_id}, should only be 1.'

            if len(results) == 0: raise KeyError('No such item_id found.')

            item_id, item_name, serial_number = results[0]

            return Item(int(item_id), item_name, serial_number)

    def get_all_items(self) -> List[Item]:
        with sqlite3.connect(self.database_filepath) as conn:
            c = conn.cursor()
            c.execute('''SELECT * FROM items''')

            results = c.fetchall()

        return [Item(int(item_id), item_name, serial_number) for item_id,item_name,serial_number in results]

    def assign_item_permanently(self, item: Item, soldier: Soldier) -> bool:
        with sqlite3.connect(self.database_filepath) as conn:
            c = conn.cursor()
            c.execute('''INSERT INTO ? VALUES (?,?)''', PERMANENT_ACCOUNTABILITY_TABLE_NAME, item.id, soldier.id)

        return True

    def unassign_item_permanently(self, item: Item):
        # TODO !!
        return super().unassign_item_permanently(item)

    def add_item(self, item: Item) -> bool:
        # TODO ensure no conflicting item ids

        with sqlite3.connect(self.database_filepath) as conn:
            c = conn.cursor()

            c.execute('''INSERT INTO ? VALUES (?,?,?)''', ITEMS_TABLE_NAME, *item)

        return True


if __name__ == '__main__':
    a = Armory()