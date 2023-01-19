import os
import sys


PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.path.pardir
))
sys.path.append(PROJECT_ROOT)


from singleton.singleton import *


if __name__ == "__main__":

    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'logger1.log'))

    logger1 = SingletonLogger(filename=filename)
    print(logger1)
    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'logger2.log'))
    logger2 = SingletonLogger(filename=filename)
    print(logger1)
    print(logger2)

    logger1 = BorgLogger(filename)
    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'logger2.log'))
    logger2 = BorgLogger(filename)

    print(logger1)
    print(logger2)
