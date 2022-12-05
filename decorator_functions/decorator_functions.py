from __future__ import annotations
from typing import Any
from ..mapping_definition.mapping_defiinition import *

def mapping(param: Mapping_m) -> list[dict[str, Any]]:
    def inner(function):
        def wrapper(*args, **kwargs):
            f = function(*args, **kwargs)
            arr_m = []
            for i in f:
                tmp_item = {GetRK_m.PROPS[key]: value for key, value in i.items()}
                arr_m.append(tmp_item)
            return arr_m
        return wrapper
    return inner

