import cx_Oracle
import requests

from const_for_api import *
from currency_classes.currency import Currency
from nb_api import NbApi
import random


class DbTools:

    @staticmethod
    def get_random_currency_statistics():
        result_list = []
        conn = cx_Oracle.connect(CONNECT)
        curs = conn.cursor()
        sql_req = ('SELECT * FROM CURRENCY_STATISTICS')
        for row in curs.execute(sql_req):
            result_list.append(row[0])
        conn.close()
        return random.choice(result_list)

    # добавляем одну забись валют
    @staticmethod
    def add_currency_to_db(currency):
        conn = cx_Oracle.connect(CONNECT)
        curs = conn.cursor()

        #возможно параметры стоило поместить внутрь {}, не знаю как лучше
        sql_req = (
                'INSERT INTO CURRENCY (CUR_ID,CUR_PARENT_ID,CUR_CODE,CUR_ABBREVIATION,CUR_NAME,CUR_NAME_BEL,CUR_NAME_ENG,CUR_QUOT_NAME,CUR_QUOT_NAME_BEL,CUR_QUOT_NAME_ENG,CUR_NAME_MULTI,CUR_NAME_BEL_MULTI,CUR_NAME_ENG_MULTI,CUR_SCALE,CUR_PERIODICITY,CUR_DATE_START,CUR_DATE_END) VALUES (\'' + '{}' + '\',\'' + '{}' + '\',\'' +
                '{}' + '\',\'' + '{}' + '\',\'' + '{}' + '\',\'' + '{}' + '\',\'' + '{}' + '\',\'' + '{}' + '\',\'' + '{}' + '\',\'' + '{}' + '\',\'' + '{}' + '\',\'' + '{}' + '\',\'' + '{}' + '\',\'' + '{}' + '\',\'' + '{}' + '\',\'' + '{}' + '\',\'' + '{}' + '\')').format(
            currency.cur_id, currency.cur_parent_id, currency.cur_code, currency.cur_abbreviation, currency.cur_name,
            str(currency.cur_name_bel).replace("'", ""), currency.cur_name_eng, currency.cur_quot_name,
            str(currency.cur_quot_name_bel).replace("'", ""), currency.cur_quot_name_eng, currency.cur_name_multi,
            str(currency.cur_name_bel_multi).replace("'", ""), currency.cur_name_eng_multi, currency.cur_scale,
            currency.cur_periodicity, currency.cur_date_start, currency.cur_date_end)
        curs.execute(sql_req)
        conn.commit()
        conn.close()

    # добавляем все записи валют
    @staticmethod
    def add_all_currencies(request=requests.get(url=ALL_CURRENCIES)):
        for i in range(0, len(request.json())):
            currencys = Currency(request.json()[i])
            DbTools.add_currency_to_db(currencys)

    # получаем все cur_id из Currency
    @staticmethod
    def get_all_cur_id():
        result_list = []
        conn = cx_Oracle.connect(CONNECT)
        curs = conn.cursor()
        sql_req = ('SELECT * FROM CURRENCY')
        for row in curs.execute(sql_req):
            result_list.append(row[0])
        conn.close()
        return result_list

    # получаем валюту из Бд с указанным CUR_id
    @staticmethod
    def get_currency_from_bd(cur_id):
        conn = cx_Oracle.connect(CONNECT)
        curs = conn.cursor()
        sql_req = ('SELECT * FROM CURRENCY WHERE CUR_ID= (\'' + str(cur_id) + '\')')
        for row in curs.execute(sql_req):
            return row
        conn.close()

    # получаем рандомный Id валюты из таблицы currency
    @staticmethod
    def get_random_currency():
        result_list = []
        conn = cx_Oracle.connect(CONNECT)
        curs = conn.cursor()
        sql_req = ('SELECT * FROM CURRENCY')
        for row in curs.execute(sql_req):
            result_list.append(row[0])
        conn.close()
        return random.choice(result_list)

    # тянем из бд конкретную статистику
    @staticmethod
    def get_currency_from_statistics_db(cur_id):
        result_list = []
        conn = cx_Oracle.connect(CONNECT)
        curs = conn.cursor()
        sql_req = ('SELECT * FROM CURRENCY_STATISTICS WHERE CUR_ID= (\'' + str(cur_id) + '\') ORDER BY CUR_DATE ASC')
        for row in curs.execute(sql_req):
            result_list.append(row)
        conn.close()
        return result_list

    @staticmethod
    def add_statistics_to_db(currency_statistics):
        conn = cx_Oracle.connect(CONNECT)
        curs = conn.cursor()
        sql_req = (
                    'INSERT INTO CURRENCY_STATISTICS (CUR_ID,CUR_DATE,CUR_OFFICIAL_RATE) VALUES (\'' + '{}' + '\',\'' + '{}' + '\',\'' + '{}' + '\')').format(
            currency_statistics.cur_id, currency_statistics.date, currency_statistics.cur_official_rate)
        curs.execute(sql_req)
        conn.commit()
        conn.close()

    @staticmethod
    def add_current_statistics_to_db(currency_statistics):
        conn = cx_Oracle.connect(CONNECT)
        curs = conn.cursor()
        sql_req = ('INSERT INTO CURRENCY_STATISTICS (CUR_ID,CUR_DATE,CUR_OFFICIAL_RATE) VALUES (\'' + str(
            currency_statistics.cur_id) + '\',\'' + str(currency_statistics.date) + '\',\'' + str(
            currency_statistics.cur_official_rate) + '\')')
        curs.execute(sql_req)
        conn.commit()
        conn.close()

    @staticmethod
    def check_is_empty(currency):

        return currency

    @staticmethod
    def add_all_statistics_to_db(list_statistics=NbApi.get_all_statistics()):
        for i in list_statistics:
            if i.cur_name_multi == '':
                i.cur_name_multi = 'emptyvalue'
            DbTools.add_statistics_to_db(i)

    @staticmethod
    def get_currency_from_stat_bd():
        result_list = []
        conn = cx_Oracle.connect(CONNECT)
        curs = conn.cursor()
        sql_req = ('SELECT * FROM CURRENCY_STATISTICS')
        conn.close()
        return result_list
