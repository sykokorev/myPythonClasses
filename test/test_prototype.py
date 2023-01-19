import os
import sys


PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.path.pardir
))
sys.path.append(PROJECT_ROOT)

from prototype.rts_prototype import *


if __name__ == "__main__":
    barracks = Barracks()
    knight = barracks.build_unit('Knight', 0)
    archer = barracks.build_unit('Archer', 1)
    print(knight, end='\n\n')
    print(archer, end='\n\n')
