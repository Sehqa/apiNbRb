import pytest
from tools.db_tools import *
from tools.compare_tools import CompareTools


def test_all_currencies_status_code_is_200():
    assert (str(NbApi.get_currencies()[0]) == str(200))


def test_get_random_currency():
    assert (NbApi.get_current_currencies(DbTools.get_random_currency())[0] == 200)


@pytest.mark.parametrize('cur_id', [1111111,'fddfdfdfd'])
@pytest.mark.parametrize('status_code', [404,400])
def test_get_random_currency(cur_id,status_code):
    assert (NbApi.get_current_currencies(str(cur_id))[0] == status_code)




def test_compare_all_currencies(fixture_all_id):
    CompareTools.compare_json_and_db_currency(fixture_all_id)


def test_compare_currency_statistics(fixture_random_statistics_from_db, fixture_random_statistics_from_api):
    fixture_random_statistics_from_api == fixture_random_statistics_from_db


@pytest.mark.parametrize('cur_id', ['510','аывыавы'])
@pytest.mark.parametrize('status_code', [200,400])
def test_get_currency_statistics(cur_id,status_code):
    assert NbApi.get_statistics_for_currency(cur_id)[1] == status_code



@pytest.mark.parametrize('cur_id', ['510','510',''])
@pytest.mark.parametrize('start_date', ['2021-11-02','','2021-12-03'])
@pytest.mark.parametrize('end_date', ['2021-12-02','2021-11-02',''])
@pytest.mark.parametrize('status_code', [200,400,400])
def test_get_currency_statistics_with_invalid_date(cur_id, start_date, end_date,status_code):
    assert NbApi.get_statistics_for_currency(cur_id, start_date, end_date)[1] == status_code



@pytest.mark.parametrize('cur_id', ['510','510','510'])
@pytest.mark.parametrize('start_date', ['2021-11-02','','2021-11-02'])
@pytest.mark.parametrize('end_date', ['2021-12-03','2021-12-03',''])
@pytest.mark.parametrize('status_code', [200,404,404])
def test_witout_parameters(cur_id, start_date, end_date,status_code):
    assert NbApi.custom_get_statistics_for_currency(cur_id, custom_parameter='') == status_code



