import requests
import const_for_api
from currency_classes.currency import Currency
from const_for_api import *
from datetime import date
from datetime import timedelta
from currency_classes.currency_statistics import *
from jsonschema import validate


class NbApi:

    @staticmethod
    def get_all_statistics():
        start_date = date.today() - timedelta(days=30)
        end_date = date.today()
        list_statistics = []
        currencies = NbApi.get_currencies()[1]
        for i in range(0, len(currencies)):
            request = requests.get(url=CURRENT_DYMANICS + str(currencies[i].get('Cur_ID')) + "?startDate=" + str(
                start_date) + "&endDate=" + str(end_date))
            if len(request.json()) != 0:
                for i in range(0, len(request.json())):
                    validate(instance=request.json()[i], schema=const_for_api.schema_statistics)
                    currency = CurrencyStatistics(request.json()[i])
                    list_statistics.append(currency)
        return list_statistics

    @staticmethod
    def get_statistics_for_currency(cur_id, start_date=date.today() - timedelta(days=30), end_date=date.today()):
        const_for_api.STATUS = 0
        list_statistics = []
        request = requests.get(url=CURRENT_DYMANICS + str(
            cur_id) + "?startDate=" + str(start_date) + "&endDate=" + str(end_date))
        if request.status_code != 200:
            return request.status_code
        elif len(request.json()) != 0:
            for i in range(0, len(request.json())):
                validate(instance=request.json()[i], schema=const_for_api.schema_statistics)
                currencys = CurrencyStatistics(request.json()[i])
                list_statistics.append(currencys)
        return list_statistics

    @staticmethod
    def get_currencies(list_currencies=[]):
        request = requests.get(url=ALL_CURRENCIES)
        for i in range(0, len(request.json())):
            validate(instance=request.json()[i], schema=const_for_api.schema_currency)
            currency_object = Currency(request.json()[i])
            list_currencies.append(currency_object)
        return [request.status_code, request.json()]

    @staticmethod
    def get_current_currencies(cur_id):
        request = requests.get(url=ALL_CURRENCIES + '/' + cur_id)
        validate(instance=request.json(), schema=const_for_api.schema_currency)
        return [request.status_code, request, request.json()]

    @staticmethod
    def custom_get_statistics_for_currency(cur_id,custom_parameter=''):
        request = requests.get(url=CURRENT_DYMANICS + str(
            cur_id) + custom_parameter)
        return request.status_code

