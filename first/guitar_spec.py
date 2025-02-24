from __future__ import annotations
from builder import Builder
from type import Type
from wood import Wood
from typing import Optional
class GuitarSpec:
    def __init__(self, builder: Builder, model: str, type: Type, back_wood: Wood, top_wood: Wood, num_strings:int) -> None:
        self._builder = builder
        self._model = model
        self._type = type
        self._back_wood = back_wood
        self._top_wood = top_wood
        self._num_strings = num_strings

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
    

    @property
    def num_strings(self) -> int:
         return self._num_strings

    def match(self, searching_guitar: GuitarSpec) -> bool:
        """ Compare builder, model, type, back_wood, top_wood"""
        guitar: GuitarSpec = self
        if searching_guitar.builder and searching_guitar.builder != guitar.builder:
            return False
        if searching_guitar.model and searching_guitar.model.lower() != guitar.model.lower():
            return False
        if searching_guitar.type and searching_guitar.type != guitar.type:
            return False
        if searching_guitar.back_wood and searching_guitar.back_wood != guitar.back_wood:
            return False
        if searching_guitar.top_wood and searching_guitar.top_wood != guitar.top_wood:
            return False
        if searching_guitar.num_strings and searching_guitar.num_strings != guitar.num_strings:
            return False
        return True
        

    def __str__(self) -> str:
            return f"builder={self._builder}, model={self._model}, type={self._type}, back_wood={self._back_wood}, top_wood={self._top_wood}, num_strings={self.num_strings}"
    