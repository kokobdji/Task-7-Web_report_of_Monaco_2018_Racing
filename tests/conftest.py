import pytest
from reporter import Driver

from web_reporter import create_app


@pytest.fixture(scope='session')
def flask_app():
    app = create_app()

    client = app.test_client()

    yield client


class ReporterTest:
    def __init__(self, order):
        self.order = order

    list_of_drivers = [Driver(name='Giorgio Novozhylov', team='Jeep', abbv='GNJ', time='3'),
                       Driver(name='Fabbio Miretti', team='Juventus', abbv='FMJ', time='1'),
                       Driver(name='Nicolo Fagioli', team='Juventus', abbv='NFJ', time='2')]

    def driver_sorting(self):
        return sorted(self.list_of_drivers, key=lambda x: x.time, reverse=self.order)

    def build_reporter(self):
        return self.list_of_drivers
