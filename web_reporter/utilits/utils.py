from reporter import Driver


def driver_info_returner(data: list[Driver], driver_id: str) -> Driver:
    for driver in data:
        if driver_id == driver.abbv:
            return driver
