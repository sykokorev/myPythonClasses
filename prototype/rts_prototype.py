import json
from copy import deepcopy


from prototype.prototype import Protoype
from prototype.const import UNITS_FILE


class Unit(Protoype):

    def __init__(self, unit_type, level):
        self.unit_type = unit_type
        self.level = level

        with open(UNITS_FILE, 'r') as units:
            data = json.load(units)[self.unit_type][self.level]
            self.life = data['life']
            self.speed = data['speed']
            self.atack_power = data['atack_power']
            self.atack_range = data['atack_range']
            self.weapon = data['weapon']

    def __str__(self):
        return f'Type: {self.unit_type}\nLevel : {self.level}\nLife : {self.life}\nSpeed : {self.speed}\n' \
                f'Atack power : {self.atack_power}\n' \
                 f'Atack Range : {self.atack_range}\n' \
                  f'Weapon : {self.weapon}'

    def clone(self):
        return deepcopy(self)


class Barracks(object):
    
    units = {
        "Knight": Unit,
        "Archer": Unit
    }

    def build_unit(self, unit_type, level):
        return self.units[unit_type](unit_type, level).clone()


