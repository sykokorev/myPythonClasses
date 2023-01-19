import json
import os


UNITS_FILE = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'units.json'
))


class Knight(object):
    
    def __init__(self, level):
        self.unit_type = "Knight"
        with open(UNITS_FILE, 'r') as units:
            data = json.load(units)['Knight'][level]
            self.level = level
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
    

class Archer(object):

    def __init__(self, level):
        self.unit_type = "Knight"
        with open(UNITS_FILE, 'r') as units:
            data = json.load(units)['Archer'][level]
            self.level = level
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


class Barracks(object):

    UNITS = {
        'Knight': Knight,
        'Archer': Archer
    }

    def generate_unit(self, unit_type, level):
        return self.UNITS[unit_type](level)
