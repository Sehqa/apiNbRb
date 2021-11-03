import pytest
from tools.db_tools import DbTools
from nb_api import NbApi
random_id_statistics=str(DbTools.get_random_currency_statistics())


@pytest.fixture(scope="function", params=DbTools.get_all_cur_id())
def fixture_all_id(request):
    return request.param

@pytest.fixture(scope="function")
def fixture_random_statistics_from_db():
    return DbTools.get_currency_from_statistics_db(random_id_statistics)

@pytest.fixture(scope="function")
def fixture_random_statistics_from_api():
    return NbApi.get_statistics_for_currency(random_id_statistics)

