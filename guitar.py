from type import Type
from builder import Builder
from wood import Wood
from guitar_spec import GuitarSpec


class Guitar:
    def __init__(self, serial_number: str, price: float, builder: Builder, model: str, type: Type, back_wood: Wood, top_wood: Wood) -> None:
        self._serial_number = serial_number
        self._price = price
        self._spec = GuitarSpec(builder=builder, model=model, type=type, back_wood=back_wood, top_wood=top_wood)
        # self._builder = builder
        # self._model = model
        # self._type = type
        # self._back_wood = back_wood
        # self._top_wood = top_wood


    @property
    def serial_number(self) ->str:
        return self._serial_number
    

    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, price: float) -> None:
        if price <= 0.0:
            raise ValueError("The price should be greater than 0.0")
        self._price = price
    
    @property
    def spec(self) -> GuitarSpec:
         return self._spec
    

    def __str__(self) -> str:
            # return f"Guitar(serial_number={self.serial_number}, price={self.price}, builder={self.spec.builder}, model={self.spec.model}, type={self.spec.type}, back_wood={self.spec.back_wood}, top_wood={self.spec.top_wood})"
            return f"Guitar(serial_number={self.serial_number}, price={self.price}, spec={self.spec})"
    
