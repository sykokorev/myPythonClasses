from abc import ABCMeta, abstractmethod


class Protoype(metaclass=ABCMeta):

    @abstractmethod
    def clone(self):
        pass
