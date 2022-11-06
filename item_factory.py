from typing import TYPE_CHECKING

import entity_factories


class ItemFactory:

    @staticmethod
    def get_instance(id: str) -> object:
        # find an item or return null
        # TODO: figure out why Item causes NameErrors
        
        if id == "health_potion":
            return entity_factories.health_potion
        elif id == "lightning_scroll":
            return entity_factories.lightning_scroll
        elif id == "confusion_scroll":
            return entity_factories.confusion_scroll
        elif id == "fireball_scroll":
            return entity_factories.fireball_scroll
        elif id == "dagger":
            return entity_factories.dagger
        elif id == "sword":
            return entity_factories.sword
        elif id == "leather_armor":
            return entity_factories.leather_armor
        elif id == "chain_mail":
            return entity_factories.chain_mail
        else:
            return None

