from __future__ import annotations
from typing import Any


class Builder():

    @property
    def real_state_property(self) -> None:
        pass

    def produce_type_property(self) -> None:
        pass

class RealStateProperty():

    def __init__(self) -> None:
        self.characteristics = []

    def add(self, characteristic: Any) -> None:
        self.characteristics.append(characteristic)

    def list_characteristics(self) -> None:
        print(f"Product parts: {', '.join(self.characteristics)}", end=" ")


class ConcreteBuilder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._real_state_property = RealStateProperty()

    @property
    def real_state_property(self) -> RealStateProperty:
        real_state_property = self._real_state_property
        self.reset()
        return real_state_property

    def produce_type_property(self, type_property: str) -> None:
        self._real_state_property.add(type_property)


class Director:

    def __init__(self) -> None:
        self._real_estate_property = None

    @property
    def real_estate_property(self) -> Builder:
        return self._real_estate_property

    @real_estate_property.setter
    def real_estate_property(self, builder: Builder) -> None:
        self._real_estate_property = builder

    def build_property(self, type_property: str) -> None:
        self.real_estate_property.produce_type_property(type_property)


if __name__ == '__main__':
    director = Director()
    builder = ConcreteBuilder()
    director.real_estate_property = builder

    director.build_property('Apartment')
    director.build_property('House')
    builder.real_state_property.list_characteristics()

    print('-------------------')

    director.build_property('House')
    builder.real_state_property.list_characteristics()
