from typing import List

from abc import ABC, abstractmethod
from armory.backend.armory.item import Item, ItemStatus
from armory.backend.armory.soldier import Soldier
from armory.backend.armory.status import ArmoryStatus

class AbstractArmory(ABC):

    @abstractmethod
    def get_item(self, item_id: int) -> Item:
        '''
            Returns the item with the item_id specified.

            Throws a KeyError if the item_id does not exist.
        '''
        raise NotImplementedError

    @abstractmethod
    def get_all_items(self) -> List[Item]:
        '''
            Returns a list of every item in this armory.
        '''
        raise NotImplementedError


    @abstractmethod
    def assign_item_permanently(self, item: Item, soldier: Soldier) -> bool:
        '''
            Assigns permanent accountability of item `item` to soldier `soldier`.

            Returns True if operation was successful, else False.
        '''
        raise NotImplementedError

    @abstractmethod
    def unassign_item_permanently(self, item: Item):
        '''
            Unassigns the specified item from all of its permanent soldiers.

            Returns True if operation was successful, else False.
        '''
        raise NotImplementedError


    @abstractmethod
    def assign_item_temporarily(self, item: Item, soldier: Soldier) -> bool:
        '''
            Assigns temporary accountability of item `item` to soldier `soldier`.

            Returns True if operation was successful, else False.
        '''
        raise NotImplementedError

    @abstractmethod
    def unassign_item_temporarily(self, item: Item):
        '''
            Unassigns the specified item from all of its temporary soldiers.

            Returns True if operation was successful, else False.
        '''
        raise NotImplementedError
    
    @abstractmethod
    def add_item(self, item: Item) -> bool:
        '''
            Add a new item to this Armory's registry.

            Returns True if operation was successful, else False. 
        '''
        raise NotImplementedError

    @abstractmethod
    def remove_item(self, item_id: int) -> bool:
        '''
            Removes an item to this Armory's registry.

            Returns True if operation was successful, else False.

            Throws a KeyError if the item was not in the armory.
        '''
        raise NotImplementedError

    @abstractmethod
    def check_item_in(self, item: Item) -> bool:
        '''
            Checks an existing item in as being present in this Armory's registry.

            Returns True if operation was successful, else False. 
        '''
        raise NotImplementedError

    @abstractmethod
    def check_item_out(self, item: Item) -> bool:
        '''
            Checks an existing item out of this Armory's registry.

            Returns True if operation was successful, else False. 
        '''
        raise NotImplementedError

    @abstractmethod
    def account_for_item(self, item: Item) -> bool:
        '''
            Accounts for this item in this Armory's registry.

            Returns True if operation was successful, else False. 
        '''
        raise NotImplementedError

    @abstractmethod
    def get_soldier(self, user_id: int) -> Soldier:
        '''
            Returns the solider with the specified user_id.

            Throws a KeyError if the user_id does not exist.
        '''
        raise NotImplementedError

    @abstractmethod
    def get_soldiers(self) -> List[Soldier]:
        '''
            Returns a list of every soldier associated with this armory.
        '''
        raise NotImplementedError

    @abstractmethod
    def reset_accountability(self) -> bool:
        '''
            Sets the status of all items in the registry to UNKNOWN.

            Returns True if operation was successful, else False. 
        '''
        raise NotImplementedError

    @abstractmethod
    def get_item_status(self, item: Item) -> ItemStatus:
        '''
            Returns the ItemStatus of the given item.
        '''
        raise NotImplementedError
    
    @abstractmethod
    def get_status(self) -> ArmoryStatus:
        '''
            Returns the status of this Armory as an ArmoryStatus.
        '''
        raise NotImplementedError
