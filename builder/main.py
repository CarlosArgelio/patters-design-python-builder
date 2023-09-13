from __future__ import annotations
from typing import Any


class Builder():

    @property
    def real_state_property(self) -> None:
        pass

    def produce_type_property(self) -> None:
        pass

    def produce_type_operation(self) -> None:
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

    def produce_type_operation(self, type_operation: str) -> None:
        self._real_state_property.add(type_operation)


class Director:

    def __init__(self) -> None:
        self._real_estate_property = None

    @property
    def real_estate_property(self) -> Builder:
        return self._real_estate_property

    @real_estate_property.setter
    def real_estate_property(self, builder: Builder) -> None:
        self._real_estate_property = builder

    def _build_property(self, build, build_data: str) -> None:

        build(build_data)

        # self.real_estate_property.produce_type_property(build_data)

    def build_type_operation(self, type_operation: str) -> None:
        self.real_estate_property.produce_type_operation(type_operation)



if __name__ == '__main__':
    director = Director()
    builder = ConcreteBuilder()
    director.real_estate_property = builder

    dict_build = {
        'typeOperation': director.build_type_operation
    }

    director._build_property(dict_build['typeOperation'], 'Venta')
    # director._build_property('Apartment')
    # director._build_property('House')
    builder.real_state_property.list_characteristics()

    # print('-------------------')

    # director._build_property('House')
    # builder.real_state_property.list_characteristics()
