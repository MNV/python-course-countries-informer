from typing import Optional

from geo.clients.shemas import CountryDTO
from geo.clients.currency import CurrencyClient
from geo.models import Country


class CurrencyService:
    """
    Сервис для работы с данными о курсах валют.
    """

    def get_currency(self, base: str) -> Optional[dict]:
        """
        Получение списка курсов валют для базовой валюты.
        :param base: Базовая валюта
        :return:
        """

        if data := CurrencyClient().get_rates(base):
            return data

        return None
