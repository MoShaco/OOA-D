from builder import Builder
from type import Type
from wood import Wood

class GuitarSpec:
    def __init__(self, builder: Builder, model: str, type: Type, back_wood: Wood, top_wood: Wood) -> None:
        self._builder = builder
        self._model = model
        self._type = type
        self._back_wood = back_wood
        self._top_wood = top_wood

    @property
    def builder(self) -> Builder:
        return self._builder
    
    @property
    def model(self) -> str:
        return self._model

    @property
    def type(self) -> Type:
        return self._type
    
    @property
    def back_wood(self) -> Wood:
        return self._back_wood
    
    @property
    def top_wood(self) -> Wood:
        return self._top_wood
    

    def __str__(self) -> str:
            return f"builder={self._builder}, model={self._model}, type={self._type}, back_wood={self._back_wood}, top_wood={self._top_wood}"
    