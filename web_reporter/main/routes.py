from flask import Blueprint, abort, render_template, request
from reporter import Reporter

from web_reporter.config import PATH_TO_FILES
from web_reporter.utilits import driver_info_returner

main_app = Blueprint('main', __name__)


@main_app.route('/')
@main_app.route('/report/')
def common_statistic():
    order = False if request.args.get('order') == 'asc' else True
    data = Reporter(PATH_TO_FILES, order_by=order)
    return render_template('main.html', list_drivers=data.driver_sorting())


@main_app.route('/report/drivers/')
def driver_stats():
    order = False if request.args.get('order') == 'asc' else True
    data = Reporter(PATH_TO_FILES, order_by=order)
    return render_template('drivers_page.html', list_drivers=data.driver_sorting())


@main_app.route('/report/drivers/<driver_id>')
def driver_info(driver_id):
    data = Reporter(PATH_TO_FILES, order_by=False).build_reporter()
    driver = driver_info_returner(data, driver_id)
    if driver:
        return render_template('info_page.html', driver=driver)
    abort(404)
