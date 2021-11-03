import pytest
from tools.db_tools import *
from tools.compare_tools import CompareTools


def test_all_currencies_status_code_is_200():
    assert (str(NbApi.get_currencies()[0]) == str(200))


def test_get_random_currency():
    assert (NbApi.get_current_currencies(DbTools.get_random_currency())[0] == 200)


@pytest.mark.parametrize('cur_id', [1111111])
def test_get_random_currency_invalid(cur_id):
    assert (NbApi.get_current_currencies(str(cur_id))[0] == 404)


@pytest.mark.parametrize('cur_id', ['fddfdfdfd'])
def test_get_random_currency_text(cur_id):
    assert (NbApi.get_current_currencies(str(cur_id))[0] == 400)


def test_compare_all_currencies(fixture_all_id):
    CompareTools.compare_random_currency(fixture_all_id)


def test_compare_currency_statistics(fixture_random_statistics_from_db, fixture_random_statistics_from_api):
    CompareTools.compare_random_statistics(fixture_random_statistics_from_db, fixture_random_statistics_from_api)


@pytest.mark.parametrize('cur_id', ['111111111111'])
def test_get_currency_statistics_with_invalid_id(cur_id):
    assert NbApi.get_statistics_for_currency(cur_id) == 404



@pytest.mark.parametrize('cur_id', ['аывыавы'])
def test_get_currency_statistics_with_invalid_value_in_id(cur_id):
    assert NbApi.get_statistics_for_currency(cur_id) == 400


@pytest.mark.parametrize('cur_id', ['510'])
@pytest.mark.parametrize('start_date', ['2021-12-03'])
@pytest.mark.parametrize('end_date', ['2021-11-02'])
def test_get_currency_statistics_with_invalid_date(cur_id,start_date,end_date):
    assert NbApi.get_statistics_for_currency(cur_id,start_date,end_date ) == 400



@pytest.mark.parametrize('cur_id', ['510'])
@pytest.mark.parametrize('start_date', [''])
@pytest.mark.parametrize('end_date', ['2021-11-02'])
def test_get_currency_statistics_with_invalid_date2(cur_id,start_date,end_date):
    assert NbApi.get_statistics_for_currency(cur_id,start_date,end_date ) == 400



@pytest.mark.parametrize('cur_id', ['510'])
@pytest.mark.parametrize('start_date', [''])
@pytest.mark.parametrize('end_date', [''])
def test_get_currency_statistics_with_invalid_date3(cur_id,start_date,end_date):
    assert NbApi.get_statistics_for_currency(cur_id,start_date,end_date ) == 400



@pytest.mark.parametrize('cur_id', ['510'])
@pytest.mark.parametrize('start_date', ['2021-12-03'])
@pytest.mark.parametrize('end_date', [''])
def test_get_currency_statistics_with_invalid_date4(cur_id,start_date,end_date):
    assert NbApi.get_statistics_for_currency(cur_id,start_date,end_date ) == 400


@pytest.mark.parametrize('cur_id', ['510'])
@pytest.mark.parametrize('start_date', ['2021-10-03'])
@pytest.mark.parametrize('end_date', ['2321-12-03'])
def test_get_currency_statistics_with_invalid_date5(cur_id,start_date,end_date):
    assert NbApi.get_statistics_for_currency(cur_id,start_date,end_date ) !=400

@pytest.mark.parametrize('cur_id', [''])
@pytest.mark.parametrize('start_date', ['2021-11-02'])
@pytest.mark.parametrize('end_date', ['2021-12-03'])
def test_get_currency_statistics_without_cur_id(cur_id,start_date,end_date):
    assert NbApi.get_statistics_for_currency(cur_id,start_date,end_date ) == 400



