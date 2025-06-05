class Item():
    def __init__(self, name, description, properties):
        self._name = name
        self._description = description
        self._properties = properties

    @property
    def name(self):
        return self._name
    
    @property 
    def description(self):
        return self._description

    @property 
    def properties(self):
        return self._properties

    @name.setter
    def name(self, value):
        self._name = value

    @description.setter
    def description(self, value):
        self._description = value

    @properties.setter
    def properties(self, value):
        self._properties = value
