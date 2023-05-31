from unittest.mock import patch

from bs4 import BeautifulSoup

from tests.conftest import ReporterTest


@patch('web_reporter.main.routes.Reporter', return_value=ReporterTest(True))
def test_common_statistic_main(mocked_class, flask_app):
    response = flask_app.get('/')
    assert response.status_code == 200
    doc = BeautifulSoup(response.text, 'html.parser')
    assert doc.find('title').string == 'Report of Monaco 2018 racing'
    assert doc.find('td').string == 'Giorgio Novozhylov'
    mocked_class.assert_called_once()


@patch('web_reporter.main.routes.Reporter', return_value=ReporterTest(True))
def test_common_statistic(mocked_driver, flask_app):
    response = flask_app.get('/report/')
    assert response.status_code == 200
    doc = BeautifulSoup(response.text, 'html.parser')
    assert doc.find('title').string == 'Report of Monaco 2018 racing'
    assert doc.find('td').string == 'Giorgio Novozhylov'
    mocked_driver.assert_called_once()


@patch('web_reporter.main.routes.Reporter', return_value=ReporterTest(True))
def test_common_statistic_desc(mocked_driver, flask_app):
    response = flask_app.get('/report/?order=desc')
    assert response.status_code == 200
    doc = BeautifulSoup(response.text, 'html.parser')
    assert doc.find('td').string == 'Giorgio Novozhylov'
    mocked_driver.assert_called_once()


@patch('web_reporter.main.routes.Reporter', return_value=ReporterTest(False))
def test_common_statistic_asc(mocked_driver, flask_app):
    response = flask_app.get('/report/?order=asc')
    assert response.status_code == 200
    doc = BeautifulSoup(response.text, 'html.parser')
    assert doc.find('td').string == 'Fabbio Miretti'
    mocked_driver.assert_called_once()


@patch('web_reporter.main.routes.Reporter', return_value=ReporterTest(False))
def test_driver_info_pos(mocked_driver, flask_app):
    response = flask_app.get('/report/drivers/GNJ')
    assert response.status_code == 200
    doc = BeautifulSoup(response.text, 'html.parser')
    assert 'Giorgio Novozhylov' in doc.find('h3').string
    mocked_driver.assert_called_once()


@patch('web_reporter.main.routes.Reporter', return_value=ReporterTest(False))
def test_driver_info_neg(mocked_driver, flask_app):
    response = flask_app.get('/report/drivers/JPG')
    assert response.status_code == 404
    doc = BeautifulSoup(response.text, 'html.parser')
    assert 'Driver is not exist' in doc.find('h1').string
    mocked_driver.assert_called_once()


@patch('web_reporter.main.routes.Reporter', return_value=ReporterTest(False))
def test_driver_stats_asc(mocked_driver, flask_app):
    response = flask_app.get('/report/drivers/?order=asc')
    assert response.status_code == 200
    doc = BeautifulSoup(response.text, 'html.parser')
    assert doc.find_all('td')[1].string == 'Fabbio Miretti'
    mocked_driver.assert_called_once()


@patch('web_reporter.main.routes.Reporter', return_value=ReporterTest(True))
def test_driver_stats_desc(mocked_driver, flask_app):
    response = flask_app.get('/report/drivers/?order=desc')
    assert response.status_code == 200
    doc = BeautifulSoup(response.text, 'html.parser')
    assert doc.find_all('td')[1].string == 'Giorgio Novozhylov'
    mocked_driver.assert_called_once()
