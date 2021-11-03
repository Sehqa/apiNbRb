from nb_api import NbApi
from tools.db_tools import DbTools


class CompareTools:
    @staticmethod
    def compare_random_statistics(data_from_db, data_from_api):
        for i in range(0, len(data_from_db)):
            assert (str(data_from_db[i][0]) == str(data_from_api[i].cur_id))
            assert (str(data_from_db[i][1]) == str(data_from_api[i].date))
            assert (str(data_from_db[i][2]) == str(data_from_api[i].cur_official_rate))

    @staticmethod
    def compare_random_currency(fixture_all_id):
        dictionary = NbApi.get_current_currencies(str(fixture_all_id))[1]
        currency_from_db = DbTools.get_currency_from_bd(str(fixture_all_id))
        assert (dictionary.json().get('Cur_ID') == int(currency_from_db[0]))
        assert(dictionary.json().get('Cur_ParentID') == int(currency_from_db[1]))
        assert(dictionary.json().get('Cur_Code') == str(currency_from_db[2]))
        assert(dictionary.json().get('Cur_Abbreviation') == str(currency_from_db[3]))
        assert(dictionary.json().get('Cur_Name') == str(currency_from_db[4]))
        assert(dictionary.json().get('Cur_Name_Bel').replace("'", "") == str(currency_from_db[5]))
        assert(dictionary.json().get('Cur_Name_Eng') == str(currency_from_db[6]))
        assert(dictionary.json().get('Cur_QuotName') == str(currency_from_db[7]))
        assert(dictionary.json().get('Cur_QuotName_Bel').replace("'", "") == str(currency_from_db[8]))
        assert(dictionary.json().get('Cur_QuotName_Eng') == str(currency_from_db[9]))
        assert(dictionary.json().get('Cur_NameMulti') == str(currency_from_db[10]).replace("emptyvalue", ""))
        assert(
            dictionary.json().get('Cur_Name_BelMulti').replace("'", "") == str(currency_from_db[11]).replace(
                "emptyvalue",
                ""))
        assert(dictionary.json().get('Cur_Name_EngMulti') == str(currency_from_db[12]).replace("emptyvalue", ""))
        assert(dictionary.json().get('Cur_Scale') == int(currency_from_db[13]))
        assert(dictionary.json().get('Cur_Periodicity') == int(currency_from_db[14]))
        assert(dictionary.json().get('Cur_DateStart') == str(currency_from_db[15]))
        assert(dictionary.json().get('Cur_DateEnd') == str(currency_from_db[16]))

