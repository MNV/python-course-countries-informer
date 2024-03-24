from typing import Optional

from geo.clients.shemas import CountryDTO, CurrencyRatesDTO
from geo.clients.currency import CurrencyClient
from geo.models import Country


class CurrencyService:
    """
    Сервис для работы с данными о курсах валют.
    """

    def get_currency(self, base: str) -> Optional[CurrencyRatesDTO]:
        """
        Получение списка курсов валют для базовой валюты.
        :param base: Базовая валюта
        :return:
        """

        data = CurrencyClient().get_rates(base)

        if data:
            return CurrencyRatesDTO(
                base=data["base"],
                date=data["date"],
                rates=data["rates"],
            )

        return None
