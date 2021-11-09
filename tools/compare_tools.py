from nb_api import NbApi
from tools.db_tools import DbTools


class CompareTools:

    @staticmethod
    def compare_json_and_db_currency(fixture_all_id):
        dictionary = NbApi.get_current_currencies(str(fixture_all_id))[1]
        currency_from_db = DbTools.get_currency_from_bd(str(fixture_all_id))
        json_dictionary = dictionary.json()
        iter_from_db = 0
        bd_dictionary = {}
        for i in json_dictionary.keys():
            json_dictionary[i] = str(json_dictionary[i])
            bd_dictionary[i] = str(currency_from_db[iter_from_db])
            iter_from_db = iter_from_db + 1
        return json_dictionary == bd_dictionary
