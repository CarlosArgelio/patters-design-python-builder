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

    def produce_categorie(self) -> None:
        pass

    def produce_parking_lot(self) -> None:
        pass

    def produce_rooms(self) -> None:
        pass

    def produce_bathrooms(self) -> None:
        pass

    def produce_mtrs2(self) -> None:
        pass

    def produce_price(self) -> None:
        pass

class RealStateProperty():

    def __init__(self) -> None:
        self.characteristics = []

    def add(self, characteristic: Any) -> None:
        self.characteristics.append(str(characteristic))

    def list_characteristics(self) -> None:
        print(f"Product parts: {', '.join(self.characteristics)}")


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

    def produce_categorie(self, categorie: str) -> None:
        self._real_state_property.add(categorie)

    def produce_parking_lot(self, parking_lot: int) -> None:
        self._real_state_property.add(parking_lot)

    def produce_rooms(self, rooms: int) -> None:
        self._real_state_property.add(rooms)

    def produce_bathrooms(self, bathrooms: int) -> None:
        self._real_state_property.add(bathrooms)

    def produce_mtrs2(self, mtrs2: int) -> None:
        self._real_state_property.add(mtrs2)

    def produce_price(self, price: float) -> None:
        self._real_state_property.add(price)

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

    def build_type_operation(self, type_operation: str) -> None:
        self.real_estate_property.produce_type_operation(type_operation)

    def build_type_property(self, type_property: str) -> None:
        self.real_estate_property.produce_type_property(type_property)

    def build_categorie(self, categorie: str) -> None:
        self.real_estate_property.produce_categorie(categorie)

    def build_parking_lot(self, parking_lot: int) -> None:
        self.real_estate_property.produce_parking_lot(parking_lot)

    def build_rooms(self, rooms: int) -> None:
        self.real_estate_property.produce_rooms(rooms)

    def build_bathrooms(self, bathrooms: int) -> None:
        self.real_estate_property.produce_bathrooms(bathrooms)

    def build_mtrs2(self, mtrs2: int) -> None:
        self.real_estate_property.produce_mtrs2(mtrs2)

    def build_price(self, price: float) -> None:
        self.real_estate_property.produce_price(price)



if __name__ == '__main__':
    director = Director()
    builder = ConcreteBuilder()
    director.real_estate_property = builder

    dict_build = {
        'typeOperation': director.build_type_operation,
        'mtrs2': director.build_mtrs2,
        'price': director.build_price,
        'typeProperty': director.build_type_property,
        'categorie': director.build_categorie,
    }

    director._build_property(dict_build['typeOperation'], 'Venta')
    director._build_property(dict_build['price'], 100.10)
    director._build_property(dict_build['mtrs2'], 40)
    builder.real_state_property.list_characteristics()
