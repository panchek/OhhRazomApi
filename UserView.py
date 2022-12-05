from __future__ import annotations
from typing import Any
from .models import *
from .decorator_functions.decorator_functions import mapping
from .mapping_definition.mapping_defiinition import *
from rest_framework_simplejwt.tokens import RefreshToken



class Users:

    def __init__(self, user_id: int = None):
        self.user_id = user_id
        self._full_name = None
        self._last_login = None

    @mapping(GetRK_m)
    def get_rk(self, fields: list[str] = ["*"]) -> list[dict[str, Any]]:
        """
        fields may be ["*"], or contain ["id", "RK", "client", "create_date", "end_date", "Stage"]
        fields = ["*"] --> means all fields
        fields may be equel to sample of columns
        Ex. fields = ["id", "RK"]
        """

        data = Rk.objects \
                .filter(client__founder__id=self.user_id) \
                .values()
        if fields != ["*"]:
            tmp_data_list = []
            for i in data:
                tmp_data_list_item = {key: value for key, value in i.items() if key in fields}
                tmp_data_list.append(tmp_data_list_item)
            data = tmp_data_list
        return list(data)

    @property
    def last_login(self):
        """
        # computed attributes
        method return last login date of user
        """

        data = User.objects    \
                .filter(id=self.user_id)    \
                .values_list("last_login")
        return data[0][0]

    @property
    def full_name(self) -> str:
        """
        # computed attributes
        method return last login date of user
        """

        data = User.objects    \
                .filter(id=self.user_id)    \
                .values("first_name", "last_name")
        full_name = list(data)[0]["first_name"] + " " + list(data)[0]["last_name"]
        return full_name if full_name != " " else "No name"

    @staticmethod
    def log_out(self, refresh_token: str) -> None:
        refresh_token = refresh_token
        token = RefreshToken(refresh_token)
        token.blacklist()

