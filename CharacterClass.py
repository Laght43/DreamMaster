from ItemClass import Item

class Character():
    def __init__(self, name: str, max_health: int, inventory_size: int):
        self._name = name
        self._max_health = max_health
        self._health = health
        self._inventory = []
        self._inventory_size = inventory_size

    @property 
    def name(self):
        return self._name

    @property 
    def max_health(self):
        return self._max_health

    @property 
    def health(self):
        return self._health

    @property 
    def inventory(self):
        return self._inventory

    @property 
    def inventory_size(self):
        return self._inventory_size

    @name.setter
    def name(self, value: str):
        self._name = value
    
    @max_health.setter
    def max_health(self, value):
        if value > 0:
            self._max_health = value
        else:
            print("Максимальне здоров'я повинне бути більшим за 0.")

    @health.setter
    def health(self, value):
        if 0 < value <= self._max_health:
            self._health = value
        else:
            print("Здоров'я не може бути меншим за 0 або більшим за максимум.")

    @inventory_size.setter
    def inventory_size(self, value: int):
        if value > 0:
            self._inventory_size = value
        else:
            print("Розмір інвентаря не може бути менше 0.")

    def pick_up_item(self, item: Item):
        if len(self._inventory) < self._inventory_size:
            self._inventory.append(item)
        else:
            print("В інвентарі недостатньо місця.")

    def throw_item(self, number: int):
        """
        Throw an item from your inventory
        """
        if len(self._inventory) == 0:
            print("Інвентар порожній.")
        elif 0 <= number < len(self._inventory):
            print("Не в межах інвентаря.")
        else:
            self._inventory.pop(choose - 1
