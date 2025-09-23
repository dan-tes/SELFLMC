import pytest

from DataBaseManager import DataBaseManager, db
from DataBaseManager.extends import DBALL, Base


# Очищаем данные из таблиц


# Создание таблиц и очистка после всех тестов


@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    Base.metadata.create_all(bind=DBALL().get_engine())
    DBALL().clear_all_data()
    yield
    DBALL().clear_all_data()


@pytest.fixture(scope="package", autouse=True)
def database_all():
    return DBALL()
