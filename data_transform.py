from itertools import chain
import datetime


def degrees_to_direction(deg):
    switcher = {
        chain(range(338, 360), range(23)): "N",
        range(23, 68): "NE",
        range(68, 113): "E",
        range(113, 158): "SE",
        range(158, 203): "S",
        range(203, 248): "SW",
        range(248, 293): "W",
        range(293, 338): "NW"
    }

    for key in switcher:
        if deg in key:
            return switcher[key]

    raise ValueError(f"Degrees {deg} cannot be converted to direction.")


def unix_timestamp_to_datetime(unix_timestamp, timezone):
    tz = datetime.timezone(datetime.timedelta(seconds=timezone))
    dt = datetime.datetime.fromtimestamp(unix_timestamp, tz=tz)
    return dt


def json_response_to_measurement(json_response):
    measurement = (
        json_response['id'],  # city_id
        json_response['weather'][0]['id'],  # weather_id
        json_response['coord']['lon'],  # lon
        json_response['coord']['lat'],  # lat
        unix_timestamp_to_datetime(json_response['dt'], json_response['timezone']),  # datetime
        json_response['main']['temp'],  # temperature
        json_response['main']['pressure'],  # pressure
        json_response['main']['humidity'],  # humidity
        json_response['wind']['speed'],  # wind_speed
        degrees_to_direction(json_response['wind']['deg']),  # wind_direction
        json_response['clouds']['all']  # cloudiness
    )

    return measurement
